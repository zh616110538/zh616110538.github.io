---
layout:        post
title:         "Who modified files in Linux"
subtitle:      "监控是哪个进程修改了文件"
date:          "2020-04-26 15:29:47 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - linux
---

# 在Linux监控是哪个进程修改了文件 #


在项目中遇到了一个问题，一个文件被修改导致出错，但是却无法查明是哪个进程改错的，遂查找解决办法。

google了一下发现了一个工具([audit](https://www.ibm.com/developerworks/cn/linux/l-lo-use-space-audit-tool/index.html))

其中提供了一系列的工具用于各种用途，我们主要需要用到的如下：
1. auditctl 配置规则的工具
2. auditsearch 搜索查看

比如，监控 /root/.ssh/authorized_keys 文件是否被修改过：

    auditctl -w /root/.ssh/authorized_keys -p war -k auth_key

- -w 指明要监控的文件
- -p awrx 要监控的操作类型，append, write, read, execute
- -k 给当前这条监控规则起个名字，方便搜索过滤

查看修改纪录：ausearch -i -k auth_key，生成报表 aureport.

<br>
参考手册：[https://linux.die.net/man/8/auditd](https://linux.die.net/man/8/auditd)