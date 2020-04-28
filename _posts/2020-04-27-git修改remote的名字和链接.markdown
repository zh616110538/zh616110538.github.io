---
layout:        post
title:         "git修改remote的名字和链接"
date:          "2020-04-27 16:46:03 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - git
---

\#查看一个远程仓库的url<br>
git remote get-url origin

\#修改远程仓库在本地的简称<br>
git remote rename origin github 

\#添加一个远程url<br>
git remote add gitee http://your-url