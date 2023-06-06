---
layout:        post
title:         "ubuntu上搭建obfs4代理"
date:          "2023-04-10 22:55:10 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - obfs4
    - tor
    - obfs4proxy
---

# 背景 #

机场的ip是有限的，如何利用有限的ip去撬动无限的ip，tor真的给了一个很好的方案

# 安装 #

    release=$(lsb_release -a 2>&1 | awk '/Codename/{print $2}')
    cat << EOF | sudo tee /etc/apt/sources.list.d/tor.list
    deb https://deb.torproject.org/torproject.org $release main
    deb-src https://deb.torproject.org/torproject.org $release main
    EOF

    curl -sS https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --import
    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 |gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/tor.gpg > /dev/null

    sudo apt update
    sudo apt install tor obfs4proxy deb.torproject.org-keyring

# 配置 #

    cat << EOF | sudo tee /etc/tor/torrc
    Socks5Proxy 127.0.0.1:1080
    SocksPort 0.0.0.0:9050
    HTTPTunnelPort 9051
    UseBridges 1
    ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
    ExitNodes {us}
    ExcludeExitNodes {cn} 
    Bridge obfs4 193.11.166.194:27025 1AE2C08904527FEA90C4C4F8C1083EA59FBC6FAF cert=ItvYZzW5tn6v3G4UnQa6Qz04Npro6e81AP70YujmK/KXwDFPTs3aHXcHp4n8Vt6w/bv8cA iat-mode=0
    EOF

    sudo systemctl start tor@default.service

**注意**：
1. SocksProxy是本地的socks5代理
2. Bride可以在[https://bridges.torproject.org/options/](https://bridges.torproject.org/options/)获取，注意获取到的桥复制过来不是直接就能用的，还得前面还得加上Bridge
3. ExitNodes可以在[https://metrics.torproject.org/rs.html#search/flag:exit%20country:us%20](https://metrics.torproject.org/rs.html#search/flag:exit%20country:us%20)获取，可以代替掉{us}，格式为`ExitNodes IP:PORT`
4. SocksPort是socks协议的代理，而HTTPTunnelPort是http协议的代理，根据需求使用


# 测试是否成功 #

    # 不使用tor
    curl ipinfo.io 
    # 使用tor
    curl -x socks5://localhost:9050 ipinfo.io 


# 参考链接 #
[https://blog.csdn.net/yeshankuangrenaaaaa/article/details/100533939](https://blog.csdn.net/yeshankuangrenaaaaa/article/details/100533939)

