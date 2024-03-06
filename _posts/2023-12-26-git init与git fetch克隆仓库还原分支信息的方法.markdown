---
layout:        post
title:         "git init与git fetch克隆仓库还原分支信息的方法"
date:          "2023-12-26 15:28:44 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - git
---

```bash
for branch in $(git branch -r | grep "^$remote_name" | sed 's/^$remote_name\///'); do
    # 检查本地分支是否已存在
    if [ "$(git branch --list $branch)" ]; then
        echo "本地分支 $branch 已存在"
    else
        # 创建本地分支并设置跟踪远程分支
        echo "创建并跟踪分支 $branch"
        git checkout -b "$branch" "$remote_name/$branch"
    fi
done
```