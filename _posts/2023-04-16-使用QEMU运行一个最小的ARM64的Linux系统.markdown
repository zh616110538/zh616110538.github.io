---
layout:        post
title:         "使用QEMU运行一个最小的ARM64的Linux系统"
date:          "2023-04-16 18:17:47 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - QEMU
---

# 步骤 #

大致步骤其实和上一篇差不多，主要一些区别在于编译时不同，这里就再记录一下

## 下载Linux源码 ##

    git clone https://github.com/torvalds/linux.git

## 编译 ##

进入仓库后编译内核

    make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- defconfig

选择要开关的功能，然后save后编译

    make -j$(nproc) ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu-

编译完后将编译好的内核取到工作目录下

    cp arch/arm64/boot/Image.gz vmlinuz

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

    wget http://ftp.cn.debian.org/debian/pool/main/b/busybox/busybox-static_1.35.0-4%2Bb2_arm64.deb -O /tmp/busybox.deb
    dpkg-deb -x /tmp/busybox.deb /tmp/busybox
    mkdir -p initramfs/bin
    mv /tmp/busybox/bin/busybox initramfs/bin

将busybox放到initramfs的bin目录下后，就可以打包了

    cd initramfs && (find . -print0 | cpio --null -ov --format=newc | gzip -9 > ../initramfs.gz) && cd ..

## 运行 ##

    qemu-system-aarch64 -M virt -cpu cortex-a57 -smp 1 -nographic -kernel vmlinuz -initrd initramfs.gz -append "console=ttyAMA0 quiet init=/init"

参数解释：<br>
* `-M virt`机器架构
* `-cpu cortex-a57`CPU架构
* `-smp 1`核心数
* `-m 128M`内存大小
* `-kernel`内核路径
* `initrd`指定initramfs
* `--nographic`不要界面
* `-append `给kernel传递的额外参数
    - `console`指定console输出的设备，注意这里时ttyAMA0，与x86-64不同
    - `init`指定init进程（init进程负责拉起所有的进程）

**BTW**:append里的init可以传两种参数，rdinit或者init，如果init不是放在/下的话，init需要改成rdinit


# 参考链接 #
* [https://unix.stackexchange.com/questions/30414/what-can-make-passing-init-path-to-program-to-the-kernel-not-start-program-as-i](https://unix.stackexchange.com/questions/30414/what-can-make-passing-init-path-to-program-to-the-kernel-not-start-program-as-i)
