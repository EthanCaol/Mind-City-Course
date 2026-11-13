---
icon: material/account-lock
---

# 编程题评分查询

期中两道编程题的答卷照片、你写下的代码，以及助教给出的评议与评分。

!!! note "验证码发到复旦学邮"
    第一次查询要先验证学号。点「获取邮箱验证码」，验证码会发到你的学邮，地址是 `学号@m.fudan.edu.cn`，收信入口 https://mail.m.fudan.edu.cn 。

    验证通过后，这台浏览器以后打开本页直接显示内容，不用再验证。换一台电脑，或者清过浏览器数据，才需要重新验证一次。

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
