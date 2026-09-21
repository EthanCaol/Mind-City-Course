/* 在线测评页面的交互。
 *
 * 这个文件全站加载（mkdocs.yml 的 extra_javascript），所以第一件事是看页面上
 * 有没有 #judge 元素 —— 没有就直接退出，别的页面不该受影响。
 *
 * 接口在 /judge/api/*，由 Caddy 反代到本机的判题服务（127.0.0.1:9100）。
 */
(function () {
  "use strict";

  var API = "/judge/api";
  var POLL_MS = 1500;
  var TOKEN_KEY = "mind-city-judge-token";

  var $ = function (id) {
    return document.getElementById(id);
  };

  /** 把文本塞进元素，用 textContent 而不是 innerHTML —— 学生输出里可能有 < > */
  function setText(node, text) {
    node.textContent = text == null ? "" : String(text);
  }

  function show(node, visible) {
    node.hidden = !visible;
  }

  function request(method, url, body) {
    var opts = { method: method, headers: {} };
    if (body !== undefined) {
      opts.headers["Content-Type"] = "application/json";
      opts.body = JSON.stringify(body);
    }
    return fetch(url, opts).then(function (resp) {
      return resp.json().then(function (data) {
        if (!resp.ok) {
          throw new Error(data.error || "请求失败（HTTP " + resp.status + "）");
        }
        return data;
      });
    });
  }

  // ---------------------------------------------------------------- 代码高亮
  //
  // textarea 本身没法给文字上色，所以背后垫一层 <pre>：两边字体、行高、内边距
  // 完全一致，textarea 的文字设成透明只留光标，滚动时把 <pre> 一起带着滚。
  //
  // 用一个正则一次扫完所有 token，比自己逐字符扫描简单得多，也够快 ——
  // 学生的作业就几十行，每次敲键重新扫一遍是微秒级。

  var C_RE =
    /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|(^[ \t]*#[^\n]*)|("(?:\\.|[^"\\\n])*"?|'(?:\\.|[^'\\\n])*'?)|\b(0[xX][0-9a-fA-F]+|\d+\.?\d*(?:[eE][+-]?\d+)?)[fFlLuU]*|\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|inline|int|long|register|restrict|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|_Bool)\b/gm;

  // 下标对应 C_RE 里的捕获组序号
  var C_CLASS = ["", "comment", "preproc", "string", "number", "keyword"];

  function highlight(text) {
    var frag = document.createDocumentFragment();
    var last = 0;
    var m;

    C_RE.lastIndex = 0;
    while ((m = C_RE.exec(text)) !== null) {
      if (m[0].length === 0) {
        C_RE.lastIndex++; // 空匹配会死循环
        continue;
      }
      if (m.index > last) {
        frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      }
      for (var g = 1; g <= 5; g++) {
        if (m[g] === undefined) continue;
        var span = document.createElement("span");
        span.className = "judge-syn judge-syn--" + C_CLASS[g];
        span.textContent = m[0];
        frag.appendChild(span);
        break;
      }
      last = m.index + m[0].length;
    }
    if (last < text.length) {
      frag.appendChild(document.createTextNode(text.slice(last)));
    }
    // 末尾补个换行：最后一行是空行时 <pre> 高度会少一行，和高亮层就对不齐了
    frag.appendChild(document.createTextNode("\n"));
    return frag;
  }

  function highlightLayer() {
    var code = $("judge-code");
    var pre = $("judge-highlight");
    return code && pre ? { code: code, pre: pre } : null;
  }

  function syncHighlight() {
    var el = highlightLayer();
    if (!el) return;
    el.pre.textContent = "";
    el.pre.appendChild(highlight(el.code.value));
    el.pre.scrollTop = el.code.scrollTop;
    el.pre.scrollLeft = el.code.scrollLeft;
  }

  // ---------------------------------------------------------------- 渲染

  function renderProgress(text) {
    var node = $("judge-progress");
    setText(node, text);
    show(node, !!text);
  }

  function renderError(message) {
    var node = $("judge-error");
    setText(node, message);
    show(node, !!message);
  }

  // gcc 的诊断行：文件:行:列: error: 消息
  var DIAG_RE = /^(.+?):(\d+):(\d+):\s*(fatal error|error|warning|note)\s*:/;
  // 指向出错列的那一行，形如 `      |         ^`
  var CARET_RE = /^\s*\|?\s*[\^~]+\s*$/;

  /**
   * 把一行 gcc 输出变成带颜色的节点。
   *
   * 全程用 DOM 节点拼，绝不用 innerHTML —— 编译器会把学生的源码原样回显出来，
   * 拼字符串就等于把学生的代码当 HTML 执行了。
   */
  function diagLine(line, severity) {
    var m = line.match(DIAG_RE);
    if (m) {
      var wrap = document.createElement("span");
      wrap.className = "judge-diag judge-diag--" + severity;

      var loc = document.createElement("span");
      loc.className = "judge-diag__loc";
      loc.textContent = m[1] + ":" + m[2] + ":" + m[3] + ": ";

      var kind = document.createElement("span");
      kind.className = "judge-diag__kind";
      kind.textContent = m[4] + ":";

      wrap.appendChild(loc);
      wrap.appendChild(kind);
      wrap.appendChild(document.createTextNode(line.slice(m[0].length)));
      return wrap;
    }

    if (CARET_RE.test(line)) {
      var caret = document.createElement("span");
      caret.className = "judge-diag__caret judge-diag__caret--" + severity;
      caret.textContent = line;
      return caret;
    }

    return null;
  }

  function renderCompileError(text) {
    var node = $("judge-compile-error");
    if (!text) {
      show(node, false);
      return;
    }

    var pre = node.querySelector("pre");
    pre.textContent = "";

    // 下面那个指列的 ^ 要跟它上面那条诊断同色，所以记着最近一条的级别
    var severity = "error";
    text.split("\n").forEach(function (line, i) {
      if (i) pre.appendChild(document.createTextNode("\n"));
      var m = line.match(DIAG_RE);
      if (m) {
        severity = /error/.test(m[4])
          ? "error"
          : m[4] === "warning"
          ? "warning"
          : "note";
      }
      pre.appendChild(diagLine(line, severity) || document.createTextNode(line));
    });
    show(node, true);
  }

  function cell(row, text, className) {
    var td = document.createElement("td");
    setText(td, text);
    if (className) td.className = className;
    row.appendChild(td);
    return td;
  }

  function renderCases(payload) {
    var box = $("judge-cases");
    box.textContent = "";

    var summary = $("judge-summary");
    if (payload.verdict === "AC") {
      summary.className = "judge-summary judge-summary--ac";
      setText(summary, "全部通过（" + payload.total + "/" + payload.total + "）");
      show(summary, true);
    } else if (payload.verdict) {
      summary.className = "judge-summary judge-summary--bad";
      setText(
        summary,
        payload.verdict_label +
          "：通过 " +
          payload.passed +
          "/" +
          payload.total +
          " 个测试点"
      );
      show(summary, true);
    } else {
      show(summary, false);
    }

    renderCompileError(payload.compile_error);
    if (!payload.cases || !payload.cases.length) {
      show(box, false);
      return;
    }

    var table = document.createElement("table");
    table.className = "judge-cases";
    var head = document.createElement("thead");
    var headRow = document.createElement("tr");
    ["测试点", "结果", "输入", "期望输出", "你的输出"].forEach(function (label) {
      var th = document.createElement("th");
      setText(th, label);
      headRow.appendChild(th);
    });
    head.appendChild(headRow);
    table.appendChild(head);

    var body = document.createElement("tbody");
    payload.cases.forEach(function (c) {
      var tr = document.createElement("tr");
      if (c.verdict !== "AC") tr.className = "judge-cases__fail";

      cell(tr, c.index, "judge-cases__idx");
      cell(tr, c.verdict_label || c.verdict, "judge-cases__verdict");

      [
        [c.stdin, c.verdict === "AC" ? "不必看" : ""],
        [c.expected, ""],
        [c.actual, ""]
      ].forEach(function (pair) {
        var text = pair[0];
        if (text && text.length > 500) text = text.slice(0, 500) + "\n…（已截断）";
        var td = cell(tr, text);
        td.className = "judge-cases__io";
      });

      body.appendChild(tr);
    });
    table.appendChild(body);
    box.appendChild(table);

    // 失败的测试点把原因写在下面，比塞进表格里好读
    var reasons = payload.cases
      .filter(function (c) {
        return c.verdict !== "AC" && c.reason;
      })
      .map(function (c) {
        return "测试点 " + c.index + "：" + c.reason;
      });
    if (reasons.length) {
      var ul = document.createElement("ul");
      ul.className = "judge-reasons";
      reasons.forEach(function (text) {
        var li = document.createElement("li");
        setText(li, text);
        ul.appendChild(li);
      });
      box.appendChild(ul);
    }

    show(box, true);
  }

  // ---------------------------------------------------------------- 流程

  var pollTimer = null;

  function stopPolling() {
    if (pollTimer) {
      clearTimeout(pollTimer);
      pollTimer = null;
    }
  }

  function poll(id, token) {
    request("GET", API + "/submissions/" + id + "?token=" + encodeURIComponent(token))
      .then(function (payload) {
        if (payload.status === "PENDING" || payload.status === "JUDGING") {
          renderProgress(
            payload.status === "PENDING"
              ? "排队中，你前面还有 " + payload.queue_ahead + " 份…"
              : "正在判题…"
          );
          pollTimer = setTimeout(function () {
            poll(id, token);
          }, POLL_MS);
          return;
        }

        stopPolling();
        renderProgress("");
        $("judge-submit").disabled = false;
        renderCases(payload);
      })
      .catch(function (err) {
        stopPolling();
        $("judge-submit").disabled = false;
        renderError(err.message);
      });
  }

  function submit() {
    var code = $("judge-code").value;
    var homework = $("judge-homework").value;

    renderError("");
    renderCompileError("");
    show($("judge-cases"), false);
    show($("judge-summary"), false);

    if (!code.trim()) {
      renderError("请先粘贴你的代码。");
      return;
    }

    $("judge-submit").disabled = true;
    renderProgress("提交中…");

    request("POST", API + "/submit", { homework: homework, code: code })
      .then(function (payload) {
        // 记住查询码，刷新页面后还能查最近这一次的结果
        try {
          localStorage.setItem(
            TOKEN_KEY,
            JSON.stringify({ id: payload.id, token: payload.token })
          );
        } catch (e) {
          /* 隐私模式下 localStorage 会抛异常，不影响判题 */
        }
        if (payload.duplicate) {
          renderError("这份代码你交过了，下面是之前的结果。");
        }
        if (payload.status === "PENDING" || payload.status === "JUDGING") {
          poll(payload.id, payload.token);
        } else {
          renderProgress("");
          $("judge-submit").disabled = false;
          renderCases(payload);
        }
      })
      .catch(function (err) {
        renderProgress("");
        $("judge-submit").disabled = false;
        renderError(err.message);
      });
  }

  function loadProblems() {
    var select = $("judge-homework");
    request("GET", API + "/problems")
      .then(function (data) {
        select.textContent = "";
        data.problems.forEach(function (p) {
          var opt = document.createElement("option");
          opt.value = p.slug;
          setText(opt, p.title + "（" + p.total_cases + " 个测试点）");
          select.appendChild(opt);
        });
        if (!data.problems.length) {
          renderError("还没有配置任何作业题目，请联系助教。");
        }
      })
      .catch(function (err) {
        renderError("连不上判题服务：" + err.message);
      });
  }

  function restoreLast() {
    var saved;
    try {
      saved = JSON.parse(localStorage.getItem(TOKEN_KEY) || "null");
    } catch (e) {
      saved = null;
    }
    if (!saved || !saved.id || !saved.token) return;

    var link = $("judge-last");
    link.href = "#";
    show(link, true);
    link.addEventListener("click", function (ev) {
      ev.preventDefault();
      renderProgress("查询中…");
      poll(saved.id, saved.token);
    });
  }

  function init() {
    if (!$("judge")) return; // 不是测评页

    loadProblems();
    restoreLast();
    $("judge-submit").addEventListener("click", submit);

    var el = highlightLayer();
    if (el) {
      syncHighlight();
      el.code.addEventListener("input", syncHighlight);
      // textarea 滚动时把背后的高亮层带着一起滚，否则两层会错位
      el.code.addEventListener("scroll", function () {
        el.pre.scrollTop = el.code.scrollTop;
        el.pre.scrollLeft = el.code.scrollLeft;
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
