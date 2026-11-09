---
name: push
description: "本笔记仓库的提交约定: 当用户说 push / 提交 / commit / 推送, 或需要把改动写进 git 提交历史时使用"
user-invocable: true
---

# 提交方式

1. 触发: 用户说 `push`, 若无其他疑问, 直接提交到远程仓库
2. 范围: 默认上传所有改动
   - 临时文件, 草稿, 临时图片一律先列出问过再动
   - 不主动 `git add`
3. 格式: 统一写成 `[26/9/29 0:14] 中文一句话简要概括`
   - 方括号内为提交时刻, 年/月/日 时:分 四段一个都不能少, 年份写两位
   - 除分钟补两位外都不补零
   - 时间不要自己拼接格式串, 直接用 `$(date '+%y/%-m/%-d %-H:%M')`
   - 概述压到一句话, 一句话写不下时空一行再补正文
   - 不用多行 `-m` 拼 patch note
4. 执行: 一条命令走完 add/commit/push, 命令保持简短
   - 不先单独执行 status/diff/date 再回来确认
5. 部署: `git push` 成功后把部署丢到后台跑, 不占用会话
   ```bash
   nohup ~/.local/bin/mind-city-deploy.sh >/var/tmp/mind-city-deploy.log 2>&1 &
   ```
   - 本机就是部署目录, push 后本地 HEAD 已是最新, 脚本里的 `git pull --ff-only` 是空操作
   - GitHub 的 webhook 已设为 inactive: 它偶发 10 秒超时且失败后不重试, 投递丢了站点会一直停在旧版, 改为本地触发
   - 脚本约 20 秒; 启动后只报告日志路径, 不等它跑完. 要确认结果看日志末尾的 `==> 部署完成` 或 `mkdocs` 的报错
   - 同一时刻只允许一个部署, 脚本自带 flock, 后到的直接跳过
