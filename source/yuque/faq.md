# 常见问题

[官方使用手册](../official-manual.md) · [语雀来源](https://alohamini.yuque.com/lq44as/tiv9xs/cyrmk57grrm79vgo) · 2026-09-28 整理

```{note}
本页的代码更新步骤已改为先检查并保存本地改动，再尝试快进更新；原文 `git restore .` 会丢弃未提交的修改。代理地址仅为局域网示例，应替换为你自己的代理服务器。
```

(yq-cyrmk57grrm79vgo-u2517d6ae)=

将树莓派中的lerobot_alohamini更新到最新版本：
1、检查并保存本地改动

(yq-cyrmk57grrm79vgo-uea5587d9)=

`git status`：先查看差异，保存你的配置和校准相关改动；存在未处理改动时先完成备份或提交。

(yq-cyrmk57grrm79vgo-u0be853b4)=

2、拉取代码

(yq-cyrmk57grrm79vgo-ud8441ecf)=

git pull --ff-only

(yq-cyrmk57grrm79vgo-u965c1d76)=

3、没有新提交时会显示 Already up to date；有更新时会列出变动。发生冲突或无法快进时，先处理分支差异。

(yq-cyrmk57grrm79vgo-u977d1848)=

(yq-cyrmk57grrm79vgo-u762fd25a)=

如果github无法访问，则设置clash允许内网访问，然后在树莓派中执行：
export http_proxy=[http://192.168.50.XXX:7890](http://192.168.50.XXX:7890)

(yq-cyrmk57grrm79vgo-u06cd1583)=

export https_proxy=[http://192.168.50.XXX:7890](http://192.168.50.XXX:7890)

(yq-cyrmk57grrm79vgo-ucc3369d5)=

(yq-cyrmk57grrm79vgo-u6c47f826)=

测试：

(yq-cyrmk57grrm79vgo-uc581c3a6)=

curl [https://github.com](https://github.com)

(yq-cyrmk57grrm79vgo-u58b10dde)=

curl https://google.com

(yq-cyrmk57grrm79vgo-u1653f7e3)=

(yq-cyrmk57grrm79vgo-u5f045e91)=

说明树莓派可以正常访问外网，此时git pull --ff-only不会再报错。
