---
id: 510
title: 树莓派raspbian设置wifi
date: 2020-01-08T15:20:06+08:00
author: Remilia Scarlet
layout: post
tags:
  - 树莓派
---
参考链接： <https://www.cnblogs.com/zhangyuejia/p/8945354.html> 

$ cat /etc/wpa\_supplicant/wpa\_supplicant.conf

ctrl\_interface=DIR=/var/run/wpa\_supplicant GROUP=netdev  
update_config=1

country=CN

network={  
ssid=&#8221;NETGEAR_5G&#8221;  
psk=&#8221;yiersansizailaiyici&#8221;  
}