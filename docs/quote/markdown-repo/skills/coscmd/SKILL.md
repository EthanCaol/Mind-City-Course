---
name: coscmd
description: 用 coscmd 操作腾讯云 COS 图床 image-1379176255 ap-shanghai, 上传, 下载, 列出, 查看, 删除图片对象, 以及替换笔记图片链接的完整流程. 当需要上传图片, 更换图床链接, 清理桶内旧文件或查看桶内容时使用
user-invocable: false
---

# COS 图床操作

腾讯云 COS, 公有读, 对象上传后即可通过公网 URL 访问

## 桶信息

| 项       | 值                                                       |
| -------- | -------------------------------------------------------- |
| Bucket   | `image-1379176255`                                       |
| AppId    | `1379176255`                                             |
| 区域     | `ap-shanghai`                                            |
| 公网前缀 | `https://image-1379176255.cos.ap-shanghai.myqcloud.com/` |

密钥不写在本文件里, 见 `Skill/PicGo配置.md`
日常操作走 `~/.cos.conf`, 用不到密钥

## 安装

```bash
pip install coscmd
```

## 初始配置

凭据存在 `~/.cos.conf`, 本机已写好
换机器或轮换密钥后重跑这一条

```bash
coscmd config -a <SecretId> -s <SecretKey> -b image-1379176255 -r ap-shanghai
```

`<SecretId>`, `<SecretKey>` 从 `Skill/PicGo配置.md` 取
配好之后, 其余子命令都不再需要传凭据

## 常用命令

```bash
coscmd list                        # 列前 100 条
coscmd list -a                     # 列全部
coscmd list -r backup/             # 按前缀列

coscmd info 20261008005016000.png  # 对象元信息
coscmd upload 本地图.png 目标.png   # 上传
coscmd download 目标.png 本地图.png # 下载
coscmd delete -f 目标.png          # 删除

coscmd signurl 目标.png -t 3600    # 生成限时签名链接
```

路径参数不带前导 `/`, 根目录直接写文件名
目录上传加 `-r`, 跳过同名同大小文件加 `-s`

## 注意事项

- `delete` 不加 `-f` 或 `-y` 会停下来询问, 在非交互环境里会一直阻塞等待输入
  - 删除一律带 `-f`
- `list` 默认只返回 100 条, 列全量要 `-a`
- Windows 下本地路径含反斜杠, 参数用引号包住
- 上传的 `Content-Type` 由扩展名推断, `.png` 会正确识别为 `image/png`
- 桶内已有 `backup/` 等目录, `list` 与 `delete -r` 注意区分前缀
  - `-r` 会删掉整个前缀下的所有对象
- 本地路径一律写绝对路径, 不要先 `cd` 再传裸文件名
  - Bash 工具每次调用都重置工作目录, `cd` 只对同一条命令的后续语句有效, 下一条里相对路径又不成立
- 报错里出现 `b'...'` 是 coscmd 按 bytes 打印的路径, 表示这个文件不存在
  - 不是引号写成两层, 按报错里的路径核对文件是否存在
- 校验对象是否上传成功统一走 `curl -sSI`, `list` 的输出不便解析

## 替换笔记图片链接的流程

1. 取原图: 从笔记里读出 URL, `curl -sSL -o src.png <url>`, 或 `coscmd download <key> src.png`
2. 处理图片, 中间产物放仓库外的临时目录
3. 生成新文件名, 规则是 `<年月日时分秒>000.png`
   末三位是同一秒的计数器, 撞了依次递增
   多个子 agent 并行上传时, 先给每个子 agent 分一个百位区间, 避免跨子 agent 撞 key
   两种 shell 各有一份写法, 取当前环境对应的那份

   ```bash
   # Bash
   K="$(date '+%Y%m%d%H%M%S')000.png"
   ```

   ```powershell
   # PowerShell
   $K = (Get-Date -Format 'yyyyMMddHHmmss') + '000.png'
   ```

   变量只在同一条命令里有效, 生成与上传要写在一起, 不能分成两次调用
4. 上传: `coscmd upload <本地图> <新key>`
5. 校验新链接: `curl -sSI <公网前缀><新key>`, 确认返回 200 与正确的 `Content-Length`
6. 再改笔记: 先 grep 整个仓库确认旧链接只出现在预期位置
   - 有第二处引用就不能删旧对象
7. 最后删旧对象: `coscmd delete -f <旧key>`

删除不可逆, 排在最后一步
前面的步骤全部验证通过再执行
