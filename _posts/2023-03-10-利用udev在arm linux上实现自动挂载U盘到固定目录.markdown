---
layout:        post
title:         "利用udev在arm linux上实现自动挂载U盘到固定目录"
date:          "2023-03-10 10:11:00 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - udev
    - linux
---

# 背景 #

项目上要实现外接硬盘，插上后自动挂载到某个目录的功能。但是插上硬盘时因为颠簸设备随时会掉线，掉线时可能还会在写入数据。所以最终要求掉线又连上的时候还能继续挂载到该目录

# 方案：使用udev实现 #

/etc/ude/rules.d/99-uto-logger.rules  

    ACTION=="add", KERNEL=="sd[a-zA-Z][0-9]", SUBSYSTEM=="block", SUBSYSTEMS=="usb",  RUN+="/usr/bin/systemd-run /usr/local/bin/logger-usb.sh add %k"
    ACTION=="remove", KERNEL=="sd[a-zA-Z][0-9]", SUBSYSTEM=="block", SUBSYSTEMS=="usb",  RUN+="/usr/bin/systemd-run /usr/local/bin/logger-usb.sh remove %k"

/usr/local/bin/logger-usb.sh

    #!/bin/bash
    ACTION=$1
    DEVBASE=$2
    MOUNT_POINT="/log_data"
    DEVICE="/dev/${DEVBASE}"

    do_mount()
    {
        mkdir -p $MOUNT_POINT
        mount $DEVICE $MOUNT_POINT
        sudo chown -R nvidia:nvidia $MOUNT_POINT
    }

    do_unmount()
    {
        umount -l $MOUNT_POINT
        rm -rf $MOUNT_POINT
    }
    case "${ACTION}" in
        add)
            do_mount
            ;;
        remove)
            do_unmount
            ;;
    esac

# 关于为什么要用systemd-run的坑 #
![](/img/20230310-140522.jpg)
systemd下的udev工作并不正常，图里的回答讲的很清楚了

# 参考链接 #  
[https://andreafortuna.org/2019/06/26/automount-usb-devices-on-linux-using-udev-and-systemd/](https://andreafortuna.org/2019/06/26/automount-usb-devices-on-linux-using-udev-and-systemd/)  
[https://blog.csdn.net/qq_37730663/article/details/105270838](https://blog.csdn.net/qq_37730663/article/details/105270838)  
[https://unix.stackexchange.com/questions/204906/linux-mount-command-returns-zero-0-but-not-working](https://unix.stackexchange.com/questions/204906/linux-mount-command-returns-zero-0-but-not-working)