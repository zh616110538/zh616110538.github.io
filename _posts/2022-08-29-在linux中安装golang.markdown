---
layout:        post
title:         "在linux中安装golang"
subtitle:      "install golang on linux"
date:          "2022-08-29 22:26:27 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - golang
---

# 目的 #
每次换机器重新安装golang都得搜教程，觉得有点麻烦，干脆自己做一个教程

# 方法 #

下载最新版本的golang安装包并且解压到`/usr/local`目录下

    curl -L -s https://golang.google.cn/dl/ |grep "<a class=\"download downloadBox\"" |grep "linux-amd64" | awk -v start="href=\"" -v end="tar.gz" '{pos1=index($0, start)+length(start); pos2=index($0, end)+length(end) ; printf "%s%s\n","https://golang.google.cn",substr($0, pos1, pos2-pos1)}' |xargs -I {} wget -c {} -O - |sudo tar -xz -C /usr/local

设置环境变量和七牛云代理

    export PATH=$PATH:/usr/local/go/bin
    go env -w GO111MODULE=on
    go env -w GOPROXY=https://goproxy.cn,direct 

路径写入文件中

    sudo bash -c 'cat << EOF >> /etc/profile
    export PATH=$PATH:/usr/local/go/bin
    EOF'