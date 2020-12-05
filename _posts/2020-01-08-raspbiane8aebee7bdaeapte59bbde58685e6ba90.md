---
id: 516
title: raspbian设置apt国内源
date: 2020-01-08T15:47:15+08:00
author: Remilia Scarlet
layout: post
tags:
  - 树莓派
---
修改/etc/apt/sources.list

root@raspberrypi:/etc/apt# cat sources.list

deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib  
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib

修改 /etc/apt/ sources.list.d/raspi.list

root@raspberrypi:/etc/apt/sources.list.d# cat raspi.list

deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui