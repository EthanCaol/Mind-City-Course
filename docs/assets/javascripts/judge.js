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
    /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|(^[ \t]*#[ \t]*\w+)|("(?:\\.|[^"\\\n])*"?|'(?:\\.|[^'\\\n])*'?)|\b(0[xX][0-9a-fA-F]+|\d+\.?\d*(?:[eE][+-]?\d+)?)[fFlLuU]*|\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|inline|int|long|register|restrict|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|_Bool)\b/gm;

  // 预处理指令后面那一段单独取色：`#include <stdio.h>` 里的头文件名在
  // GitHub Dark 主题里是字符串色，`#define MAX_ROWS` 里的宏名是紫色。
  var PREPROC_TAIL_RE = /^[ \t]*(<[^>\n]*>|[A-Za-z_]\w*)/;

  // 下标对应 C_RE 里的捕获组序号
  var C_CLASS = ["", "comment", "preproc", "string", "number", "keyword"];

  function highlight(text) {
    var frag = document.createDocumentFragment();

    function emit(from, to, cls) {
      if (to <= from) return;
      var piece = text.slice(from, to);
      if (!cls) {
        frag.appendChild(document.createTextNode(piece));
        return;
      }
      var span = document.createElement("span");
      span.className = "judge-syn judge-syn--" + cls;
      span.textContent = piece;
      frag.appendChild(span);
    }

    var last = 0;
    var m;
    C_RE.lastIndex = 0;

    while ((m = C_RE.exec(text)) !== null) {
      if (m[0].length === 0) {
        C_RE.lastIndex++; // 空匹配会死循环
        continue;
      }

      var cls = null;
      for (var g = 1; g <= 5; g++) {
        if (m[g] !== undefined) {
          cls = C_CLASS[g];
          break;
        }
      }

      emit(last, m.index, null);
      emit(m.index, m.index + m[0].length, cls);
      last = m.index + m[0].length;

      // 预处理行：指令本身已经染好了，后面跟着的头文件名 / 宏名单独取色。
      // 在这里显式吃掉那一段，而不是往主正则里加规则 —— 加规则会误伤
      // `a<b>c` 这类比较表达式。
      if (cls === "preproc") {
        var tail = PREPROC_TAIL_RE.exec(text.slice(last));
        if (tail) {
          var start = last + tail[0].indexOf(tail[1]);
          emit(last, start, null);
          emit(start, start + tail[1].length, tail[1][0] === "<" ? "string" : "macro");
          last = start + tail[1].length;
          C_RE.lastIndex = last;
        }
      }
    }

    emit(last, text.length, null);
    // 末尾补个换行：最后一行是空行时 <pre> 高度会少一行，和高亮层就对不齐了
    frag.appendChild(document.createTextNode("\n"));
    return frag;
  }

  function editorLayers() {
    var code = $("judge-code");
    var pre = $("judge-highlight");
    var gutter = $("judge-gutter");
    return code && pre && gutter ? { code: code, pre: pre, gutter: gutter } : null;
  }

  function syncHighlight() {
    var el = editorLayers();
    if (!el) return;

    el.pre.textContent = "";
    el.pre.appendChild(highlight(el.code.value));
    renderGutter(el);
    syncScroll(el);
  }

  /** 行号。层数和源码行数严格对应，否则会和右边错行。 */
  function renderGutter(el) {
    // split("\n") 的长度就是行数：末尾有空行时也会算进去，
    // 正好和高亮层末尾补的那个换行对齐
    var count = el.code.value.split("\n").length;
    var numbers = new Array(count);
    for (var i = 0; i < count; i++) numbers[i] = i + 1;
    el.gutter.textContent = numbers.join("\n") + "\n";
  }

  /** 三层一起滚。行号列只跟上下，不跟左右。 */
  function syncScroll(el) {
    el.pre.scrollTop = el.code.scrollTop;
    el.pre.scrollLeft = el.code.scrollLeft;
    el.gutter.scrollTop = el.code.scrollTop;
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
    var homework = boundHomework();

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

  /** 页面绑定的作业：`<div id="judge" data-homework="作业1">`。
   *  编辑框长在作业页面里，所以作业是页面写死的，不用下拉框选。 */
  function boundHomework() {
    var root = $("judge");
    return root ? root.getAttribute("data-homework") || "" : "";
  }

  // ------------------------------------------------------------ 作业完成情况

  function renderGrades(host, data) {
    host.textContent = "";

    if (!data.students.length) {
      host.textContent = "名单是空的。";
      return;
    }

    var table = document.createElement("table");
    table.className = "grades";

    var head = document.createElement("thead");
    var headRow = document.createElement("tr");
    var corner = document.createElement("th");
    corner.className = "grades__name";
    setText(corner, "姓名");
    headRow.appendChild(corner);

    data.homeworks.forEach(function (hw) {
      var th = document.createElement("th");
      setText(th, hw.slug);
      th.title = hw.title;
      headRow.appendChild(th);
    });
    head.appendChild(headRow);
    table.appendChild(head);

    var body = document.createElement("tbody");
    data.students.forEach(function (student) {
      var tr = document.createElement("tr");

      var name = document.createElement("td");
      name.className = "grades__name";
      setText(name, student.name);
      tr.appendChild(name);

      data.homeworks.forEach(function (hw) {
        var td = document.createElement("td");
        td.className = "grades__cell";
        if (student.passed[hw.slug]) {
          setText(td, "✅");
          td.title = student.name + "：" + hw.title + " 已通过";
        }
        tr.appendChild(td);
      });

      body.appendChild(tr);
    });
    table.appendChild(body);
    host.appendChild(table);
  }

  function loadGrades() {
    var host = $("grades");
    if (!host) return;

    request("GET", API + "/grades")
      .then(function (data) {
        renderGrades(host, data);
      })
      .catch(function (err) {
        setText(host, "读取失败：" + err.message);
      });
  }

  function init() {
    loadGrades(); // 「作业完成情况」页

    if (!$("judge")) return; // 剩下的是作业页才需要的东西

    if (!boundHomework()) {
      renderError("这个页面没有配置作业编号（data-homework），请联系助教。");
      return;
    }

    $("judge-submit").addEventListener("click", submit);

    var el = editorLayers();
    if (el) {
      syncHighlight();
      el.code.addEventListener("input", syncHighlight);
      // textarea 滚动时把行号列和高亮层带着一起滚，否则几层会错位
      el.code.addEventListener("scroll", function () {
        syncScroll(el);
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
