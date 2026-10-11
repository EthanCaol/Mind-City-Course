/* 复制公式时把渲染结果换成原始 LaTeX。

   MathJax 两种输出都不给文字：SVG 把字形画成 <path>，CHTML 的字符由运行时生成的
   CSS `content` 提供。框选下来要么是空的，要么是一堆没有意义的字符。

   MathJax 把每条公式的原始 TeX 和它对应的 mjx-container 留在 startup.document.math
   里。这里在 copy 事件里把选区克隆出来，逐个换成 `$…$`（行间公式用 `$$…$$`），
   再写回剪贴板。选区里除公式以外的文字原样保留。

   全站加载，MathJax 没接管（页面上没有公式）时直接退出。 */

const TEX_OF = () => {
  const math = window.MathJax?.startup?.document?.math;
  if (!math) return null;
  return new Map(
    math.map((item) => {
      const wrap = item.display ? '$$' : '$';
      return [item.typesetRoot, wrap + item.math + wrap];
    }),
  );
};

document.addEventListener('copy', (event) => {
  const selection = window.getSelection();
  if (!selection || selection.isCollapsed || selection.rangeCount === 0) return;

  const tex = TEX_OF();
  if (!tex) return;

  const fragment = selection.getRangeAt(0).cloneContents();
  const containers = fragment.querySelectorAll('mjx-container');
  if (containers.length === 0) return;

  for (const node of containers) {
    node.replaceWith(document.createTextNode(tex.get(node) ?? ''));
  }
  // nl2br 把段内换行渲染成 <br>，它的 textContent 是空的，不换回来会丢换行。
  for (const br of fragment.querySelectorAll('br')) {
    br.replaceWith(document.createTextNode('\n'));
  }

  event.clipboardData.setData('text/plain', fragment.textContent);
  event.preventDefault();
});
