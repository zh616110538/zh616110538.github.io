---
layout:        post
title:         "github更新https的密码策略"
date:          "2021-03-09 15:09:35 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - github
    - git
---
# 背景

由于github的安全策略更新([Token authentication requirements for Git operations](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ "Token authentication requirements for Git operations")),原来使用git credential存储的密码将无法继续使用。如果还想继续使用https的方式push到github，需要通过github生成一个token作为密码。

# 生成token
参考[Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token "Creating a personal access token")


浏览器打开[https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)

填写Note  
勾选Repo、workflow、user:email

![screenshot](/img/gitoauth.png)
完成后点击生成

接下来将生成的字符串作为密码在git clone时填入即可

# 将token添加到git中
首先设置credential.helper为存储模式

    git config --global credential.helper store

然后下次通过https操作github的时候输入账号和token即可

    git clone https://github.com/username/repo.git

**注意：如果以前用过该方法的，可以直接到~/.git-credentials修改**

# 参考链接
[https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage "https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage")

