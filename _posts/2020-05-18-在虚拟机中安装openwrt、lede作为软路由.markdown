---
layout:        post
title:         "在虚拟机中安装openwrt/lede作为软路由"
date:          "2020-05-18 14:06:50 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - openwrt
    - lede
---

## 下载lede镜像 ##
下载链接：[http://firmware.koolshare.cn/LEDE_X64_fw867/](http://firmware.koolshare.cn/LEDE_X64_fw867/)，选择uefi-gpt-squashfs.img.gz这个包<br>
下载后需要将格式转换成为vmdk格式，这里我使用了qemu-utils里的一个工具

    sudo apt install qemu-utils
    qemu-img convert -f raw -O vmdk openwrt-koolshare-mod-v2.33-r12074-007caa48d1-x86-64-uefi-gpt-squashfs.img openwrt.vmdk

## 配置vmware ##
先新建一个正常的虚拟机（不选择镜像），唯一的不同就是网络选择为桥接模式，在最后一步设备中勾选复制物理网络连接状态。创建完毕后用上一步的vmdk文件替换掉当前的vmdk文件即可。

## 配置openwrt ##
启动虚拟机等待系统启动完成，修改/etc/config/network文件，将lan的配置设为当前局域网的ip（用dhcp也行），wan也是同样设置（之所以需要配置lan和wan，是因为默认的防火墙规则配置了lan口转发到wan口的规则）<br>
**注意这里网卡不要用桥接,因为只有一个网卡，即得作wan又得作lan**

<pre>config interface 'lan'
        option ifname 'eth0'
        option proto 'static'
        option netmask '255.255.255.0'
        option multipath 'off'
        option ipaddr '192.168.100.116'

config interface 'WAN'
        option proto 'dhcp'
        option ifname 'eth0'</pre>

设置完成后重启网络

    /etc/init.d/network restart

至此配置已经完成，将局域网中的其他设备的网关设置成lan的ip即可（宿主机也可以这么设置）。另外在浏览器中输入openwrt的ip地址即可进入管理界面。

## 关于某不科学的上网插件 ##
因为已经下架了所以就[贴个链接](https://github.com/hq450/fancyss_history_package/tree/master/fancyss_X64)

## 参考链接 ##
[https://github.com/ChenWenBrian/ChenWenBrian.github.io/blob/master/blog/openwrt-for-vm.md](https://github.com/ChenWenBrian/ChenWenBrian.github.io/blob/master/blog/openwrt-for-vm.md)<br>
[https://cokebar.info/archives/2444](https://cokebar.info/archives/2444)<br>
[http://iqotom.com/?p=1234](http://iqotom.com/?p=1234)