---
icon: material/account-lock
---

# 编程题评分查询

按学号显示期中考试两道编程题的答卷照片、代码，以及助教的评议和评分。

!!! note "验证码发到复旦学邮"
    查询前先验证学号。点「获取邮箱验证码」，验证码发到该学号对应的复旦学邮，地址格式是 `学号@m.fudan.edu.cn`，收信入口 <https://mail.m.fudan.edu.cn>

    验证一次后，同一台浏览器再打开本页不再需要验证；换一台电脑或清过浏览器数据，需要重新验证。

<div class="midterm" id="midterm">
  <div class="midterm__auth" id="midterm-auth">
    <div class="midterm__row">
      <label class="midterm__label" for="midterm-id">学号</label>
      <input id="midterm-id" class="midterm__input" type="text" inputmode="numeric" maxlength="11" autocomplete="off" placeholder="11位学号">
      <button id="midterm-send" type="button">获取邮箱验证码</button>
    </div>
    <div class="midterm__row">
      <label class="midterm__label" for="midterm-code">验证码</label>
      <input id="midterm-code" class="midterm__input midterm__input--code" type="text" inputmode="numeric" maxlength="6" autocomplete="one-time-code" placeholder="6位验证码">
      <button id="midterm-login" type="button">认证登录</button>
    </div>
    <p class="midterm__msg" id="midterm-message" hidden></p>
  </div>

  <div id="midterm-result" hidden></div>
</div>
