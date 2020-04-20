---
layout:        post
title:         "How to selectively merge or pick changes from another branch in Git"
subtitle:      "在git所有的分支中提交某一个修改"
date:          "2020-04-20 16:54:19 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - git
---

# 问题背景 #
今天在项目中发现了基础部分的一个bug，涉及到所有分支都需要改。项目使用的版本管理软件是git。

# 需求 #
现在在master分支上已经修改了问题，需要将修改的部分快速的推送到所有分支。

# 方案 #
使用git checkout命令可以解决该问题
git checkout dev
git checkout -p master path/to/file
git commit -m ""


> 参考链接：[https://stackoverflow.com/questions/449541/how-to-selectively-merge-or-pick-changes-from-another-branch-in-git](https://stackoverflow.com/questions/449541/how-to-selectively-merge-or-pick-changes-from-another-branch-in-git)