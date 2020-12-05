---
id: 271
title: 设置socket端口重用失败的问题
date: 2019-06-28T13:37:08+08:00
author: Remilia Scarlet
layout: post
tags:
  - C++
---
使用函数setsockopt可以设置端口在进程退出时释放，不会出现再次启动时绑定端口失败的问题

setsockopt(sfd, SOL\_SOCKET, SO\_REUSEADDR, &reuse, sizeof(reuse)

现在出现问题该函数无效，解决方案先设置属性再调bind函数