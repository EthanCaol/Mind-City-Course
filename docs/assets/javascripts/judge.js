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
    autosize(el);
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

  /** 输入框随内容变长。高度改在容器上 —— 三层都挂在容器上，改它才是三层一起长。
   *
   *  已经撑高过就先清回 CSS 里的基线值再量：textarea 的 scrollHeight 在内容装得下
   *  时等于自身高度，不清回去量到的永远是「和现在一样高」，删行就缩不回来。
   *  还在基线上就不用清 —— 少一次强制排版，也不会先缩一下再撑开。 */
  function autosize(el) {
    var ed = el.code.parentNode;
    var code = el.code;

    if (ed.style.height) ed.style.height = "";

    // 容器上下边框，加 textarea 自己的滚动条（有的话）：少这几像素内容就真溢出。
    // 层是贴着容器的 padding box 排的，所以边框只有容器那两像素要补。
    var extra =
      (code.offsetHeight - code.clientHeight) + (ed.offsetHeight - ed.clientHeight);
    var need = code.scrollHeight + extra;

    if (need > ed.offsetHeight) ed.style.height = need + "px";
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

  // ------------------------------------------------------------ 完成情况表格
  //
  // 「作业完成情况」和「阅读进度」共用这套渲染：行是学生，列是作业/文档，
  // 格子里一个勾。两个接口（/api/grades、/api/reads）返回的结构完全一样
  // （columns + students[].done），所以后端那边也是同一段代码生成的。

  function renderGrid(host, data) {
    host.textContent = "";

    if (!data.students.length) {
      host.textContent = "名单是空的。";
      return;
    }

    // 横向滚动条做在表格**上面**。CSS 挪不动容器自己的滚动条（只能在下边），
    // 所以另做一个光杆 div，跟真正的滚动区双向镜像 scrollLeft。
    // 74 行的表，滚动条在底下的话得先滚到表尾才够得着。
    var bar = document.createElement("div");
    bar.className = "matrix__bar";
    var barInner = document.createElement("div");
    bar.appendChild(barInner);

    var scroll = document.createElement("div");
    scroll.className = "matrix__scroll";

    var table = document.createElement("table");
    table.className = "matrix";

    var head = document.createElement("thead");
    var headRow = document.createElement("tr");
    var corner = document.createElement("th");
    corner.className = "matrix__name";
    setText(corner, "姓名");
    headRow.appendChild(corner);

    data.columns.forEach(function (col) {
      var th = document.createElement("th");
      setText(th, col.slug);
      th.title = col.title;
      headRow.appendChild(th);
    });
    head.appendChild(headRow);
    table.appendChild(head);

    var body = document.createElement("tbody");
    data.students.forEach(function (student) {
      var tr = document.createElement("tr");

      var name = document.createElement("td");
      name.className = "matrix__name";
      setText(name, student.name);
      tr.appendChild(name);

      data.columns.forEach(function (col) {
        var td = document.createElement("td");
        td.className = "matrix__cell";
        if (student.done[col.slug]) {
          setText(td, "✅");
          td.title = student.name + "：" + col.title + " 已完成";
        }
        tr.appendChild(td);
      });

      body.appendChild(tr);
    });
    table.appendChild(body);
    scroll.appendChild(table);
    host.appendChild(bar);
    host.appendChild(scroll);

    // 两条滚动条互相镜像。scroll 事件是异步派发的，用标志位挡不住回环 ——
    // 直接比数值：相等就什么都不做，来回赋值自然收敛。
    function mirror(from, to) {
      if (to.scrollLeft !== from.scrollLeft) to.scrollLeft = from.scrollLeft;
    }
    scroll.addEventListener("scroll", function () {
      mirror(scroll, bar);
    });
    bar.addEventListener("scroll", function () {
      mirror(bar, scroll);
    });

    // 假滚动条的滚动范围得跟表格一样宽，一条对一条才能同步到底。
    // 表格不溢出时整条收起来。宽度要等表格进了 DOM 才量得到。
    function layout() {
      barInner.style.width = table.scrollWidth + "px";
      bar.hidden = table.scrollWidth <= scroll.clientWidth;
    }
    layout();
    // 窗口变窄可能从「不溢出」变成「溢出」。一张页面上这个表格只渲染一次，
    // 所以监听器不会越积越多。
    window.addEventListener("resize", layout);
  }

  function loadGrid(host, url) {
    if (!host) return;

    request("GET", url)
      .then(function (data) {
        renderGrid(host, data);
      })
      .catch(function (err) {
        setText(host, "读取失败：" + err.message);
      });
  }

  // ------------------------------------------------------------ 阅读登记
  //
  // 实验课页面末尾那一栏。学生填学号点一下，助教就知道他读到哪了。
  //
  // 学号记在 localStorage 里，下次打开同一篇就能直接显示「已登记」，不用重填。
  // 存不上（隐私模式、被禁用）就静默跳过 —— 那不致命，不该让「登记成功了」
  // 显示成报错。

  var SID_KEY = "mind-city.student-id";
  var NAME_KEY = "mind-city.student-name";

  function rememberedSid() {
    try {
      return localStorage.getItem(SID_KEY) || "";
    } catch (e) {
      return "";
    }
  }

  function rememberSid(sid) {
    try {
      localStorage.setItem(SID_KEY, sid);
    } catch (e) {
      /* 记不住就算了 */
    }
  }

  /** 姓名只用来做那句「×× 同学，恭喜…」。存在本地是为了下次打开不用再问服务端
      （GET 那个接口故意不查花名册），换台电脑就拿不到，退回不带姓名的说法。 */
  function rememberedName() {
    try {
      return localStorage.getItem(NAME_KEY) || "";
    } catch (e) {
      return "";
    }
  }

  function rememberName(name) {
    try {
      localStorage.setItem(NAME_KEY, name || "");
    } catch (e) {
      /* 记不住就算了 */
    }
  }

  /** 状态行：登记成功的恭喜、出错的红字，共用这一个元素。
      kind 传 "done" 或 "bad"；不传就是普通提示。 */
  function renderReadNote(text, kind) {
    var node = $("read-note");
    node.className = "read__note" + (kind ? " read__note--" + kind : "");
    setText(node, text);
    show(node, !!text);
  }

  /** 登记过之后：输入框和按钮都留着不动，只在下面加一行恭喜。
      name 拿不到时不硬凑，用不带姓名的说法。 */
  function markRegistered(name) {
    var who = name ? name + " 同学，恭喜" : "恭喜同学，";
    renderReadNote("✅ " + who + "你已经完成了这篇文档的配置流程", "done");
  }

  function submitRead(page) {
    var sid = $("read-id").value.trim();

    if (!/^[0-9]{11}$/.test(sid)) {
      renderReadNote("学号是 11 位数字，请检查一下。", "bad");
      return;
    }

    renderReadNote("");
    $("read-submit").disabled = true;
    request("POST", API + "/read", { page: page, student_id: sid })
      .then(function (data) {
        rememberSid(sid);
        rememberName(data.name);
        markRegistered(data.name);
      })
      .catch(function (err) {
        $("read-submit").disabled = false;
        renderReadNote(err.message, "bad");
      });
  }

  function initRead() {
    var root = $("read");
    if (!root) return;

    var page = root.getAttribute("data-page") || "";
    if (!page) {
      renderReadNote("这个页面没有配置页面编号（data-page），请联系助教。", "bad");
      return;
    }

    $("read-submit").addEventListener("click", function () {
      submitRead(page);
    });

    // 输入框里按回车等同于点「我已读完」。按钮在提交期间是禁用的，
    // 这里跟着一起挡，免得连按回车重复提交。
    $("read-id").addEventListener("keydown", function (e) {
      if (e.key !== "Enter") return;
      e.preventDefault();
      if ($("read-submit").disabled) return;
      submitRead(page);
    });

    var sid = rememberedSid();
    if (!sid) return;

    // 上次填过，先回填再问一次状态。查不动就算了，不打扰正在读文档的人。
    $("read-id").value = sid;
    request("GET", API + "/read?page=" + encodeURIComponent(page) +
      "&sid=" + encodeURIComponent(sid))
      .then(function (data) {
        if (data.registered) markRegistered(rememberedName());
      })
      .catch(function () {});
  }

  function init() {
    loadGrid($("grades"), API + "/grades"); // 「作业完成情况」页
    loadGrid($("reads"), API + "/reads"); // 「阅读进度」页
    initRead(); // 实验课页面末尾的登记栏

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
