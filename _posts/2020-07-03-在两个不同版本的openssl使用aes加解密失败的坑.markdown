---
layout:        post
title:         "在两个不同版本的openssl使用aes加解密失败的坑"
date:          "2020-07-03 10:16:32 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - openssl
    - aes
---

## 问题现象 ##
利用openssl1.0.2版本的的aes加密后在openssl1.1.0版本会解密失败

1.0.2版本加密

    $ openssl aes-128-cbc -salt -k password -in filename -out filename.enc 

1.1.0版本解密

    $ openssl aes-128-cbc -salt -k password -in filename.enc -out filename -d
    bad decrypt

## 原因 ##
默认摘要在Openssl 1.1中从MD5更改为SHA256

## 解决办法 ##
在加密和解密的参数中均加上-md sha256

    $ openssl aes-128-cbc -salt -k password -in filename -out filename.enc -md sha256
    $ openssl aes-128-cbc -salt -k password -in filename.enc -out filename -md sha256 -d

**注意这里不推荐使用md5作为摘要算法，因为md5**

## 参考链接 ##

[加密/解密在两个不同的openssl版本之间不能很好地工作](https://www.thinbug.com/q/39637388)<br>
[openssl FAQ](https://www.openssl.org/docs/faq.html#USER3)