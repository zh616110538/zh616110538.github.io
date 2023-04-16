---
layout:        post
title:         "利用QEMU运行Linux内核"
date:          "2023-04-16 15:14:32 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - QEMU
---

# 步骤 #

## 下载Linux源码 ##

    git clone https://github.com/torvalds/linux.git

## 编译 ##

进入仓库后编译内核

    make menuconfig

或者创建一个默认的.config

    make defconfig

选择要开关的功能，然后save后编译

    make -j$(nproc)

编译完后将编译好的内核取到工作目录下

    cp arch/x86/boot/bzImage vmlinuz

## 制作initramfs ##

创建init进程

    mkdir initramfs

    cat << EOF >> initramfs/init
    #!/bin/busybox sh
    /bin/busybox sh
    /bin/busybox poweroff -f
    EOF

    chmod +x initramfs/init

这里创建并将静态编译的busybox放进去  
这里我的busybox没有自己编译，直接从[http://ftp.cn.debian.org/debian/pool/main/b/busybox/](http://ftp.cn.debian.org/debian/pool/main/b/busybox/)扣了一个出来

    wget http://ftp.cn.debian.org/debian/pool/main/b/busybox/busybox-static_1.36.0-1~exp1_amd64.deb -O /tmp/busybox.deb
    dpkg-deb -x /tmp/busybox.deb /tmp/busybox
    mkdir -p initramfs/bin
    mv /tmp/busybox/bin/busybox initramfs/bin

将busybox放到initramfs的bin目录下后，就可以打包了

    cd initramfs && (find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../initramfs.gz) && cd ..

## 运行 ##

     qemu-system-x86_64 -m 128M -kernel vmlinuz -initrd initramfs.gz -nographic -append "console=ttyS0 init=/init"

参数解释：<br>
* `-m 128M`内存大小
* `-kernel`内核路径
* `initrd`指定initramfs
* `--nographic`不要界面
* `-append `给kernel传递的额外参数
    - `console`指定console输出的设备
    - `init`指定init进程（init进程负责拉起所有的进程）


# 参考链接 #
* [https://medium.com/@kiky.tokamuro/creating-initramfs-5cca9b524b5a](https://medium.com/@kiky.tokamuro/creating-initramfs-5cca9b524b5a)
* [http://ftp.cn.debian.org/debian/pool/main/b/busybox/](http://ftp.cn.debian.org/debian/pool/main/b/busybox/)

