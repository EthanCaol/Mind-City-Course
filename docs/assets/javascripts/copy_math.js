/* 复制公式时把渲染结果换成原始 LaTeX。

   MathJax 两种输出都不给文字：SVG 把字形画成 <path>，CHTML 的字符由运行时生成的
   CSS `content` 提供。框选下来要么是空的，要么是一堆没有意义的字符。

   MathJax 把每条公式的原始 TeX 和它对应的 mjx-container 留在 startup.document.math
   里。这里在 copy 事件里先把选区覆盖到的公式标上 TeX，再克隆选区、按标记替换，
   最后写回剪贴板。选区里除公式以外的文字原样保留。

   标记写到节点上而不是查表：克隆出来的是副本，拿副本去查原来的表查不到。
   写标记还有个好处 —— 选区边界落在公式中间时，克隆出的半个容器也带着标记。

   全站加载，MathJax 没接管（页面上没有公式）时直接退出。 */

const MARK = 'data-copy-tex';

document.addEventListener('copy', (event) => {
  const selection = window.getSelection();
  if (!selection || selection.isCollapsed || selection.rangeCount === 0) return;

  const math = window.MathJax?.startup?.document?.math;
  if (!math) return;

  const range = selection.getRangeAt(0);
  const tex = new Map(math.map((item) => [item.typesetRoot, item]));

  const marked = [];
  for (const node of document.querySelectorAll('mjx-container')) {
    const item = tex.get(node);
    if (!item || !range.intersectsNode(node)) continue;
    const wrap = item.display ? '$$' : '$';
    node.setAttribute(MARK, wrap + item.math + wrap);
    marked.push(node);
  }
  if (marked.length === 0) return;

  const fragment = range.cloneContents();
  for (const node of fragment.querySelectorAll('mjx-container')) {
    const source = node.getAttribute(MARK);
    if (source !== null) node.replaceWith(document.createTextNode(source));
  }
  for (const node of marked) node.removeAttribute(MARK);

  // nl2br 把段内换行渲染成 <br>，它的 textContent 是空的，不换回来会丢换行。
  for (const br of fragment.querySelectorAll('br')) {
    br.replaceWith(document.createTextNode('\n'));
  }

  event.clipboardData.setData('text/plain', fragment.textContent);
  event.preventDefault();
});
