---
layout:        post
title:         "ubuntu中安装samba服务"
date:          "2021-03-05 16:58:00 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - ubuntu
    - samba
    - linux
---

## 1.更新当前软件

sudo apt-get upgrade 
sudo apt-get update 
sudo apt-get dist-upgrade

## 2.安装samba服务器
sudo apt-get install samba samba-common

## 3.添加用户
sudo smbpasswd -a pi

## 4.配置samba的配置文件
vim /etc/samba/smb.conf

在配置文件smb.conf的最后添加下面的内容：<br>
[mnt]<br>
   path = /home/pi/workspace<br>
   writeable = yes<br>
   public = no<br>
   
#参考链接
[https://www.linuxidc.com/Linux/2018-11/155466.htm](https://www.linuxidc.com/Linux/2018-11/155466.htm "https://www.linuxidc.com/Linux/2018-11/155466.htm")
