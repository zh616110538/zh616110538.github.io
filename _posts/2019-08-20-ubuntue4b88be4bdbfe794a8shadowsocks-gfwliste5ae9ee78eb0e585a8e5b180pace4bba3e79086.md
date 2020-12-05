---
id: 450
title: Ubuntu下使用GFWlist实现全局pac代理
date: 2019-08-20T20:16:13+08:00
author: Remilia Scarlet
layout: post
tags:
  - Linux运维
---
转载自<https://my.oschina.net/Hgladiator/blog/761982>

1.安装[genpac](https://github.com/JinnLynn/genpac)

  * sudo apt-get install python-pip python-dev build-essential
  * sudo pip install &#8211;upgrade pip
  * sudo pip install &#8211;upgrade virtualenv
  * sudo pip install genpac
  * sudo pip install &#8211;upgrade genpac

2.为了方便管理生成的pac文件，我们在/home/目录下新建一个文件夹，命名为proxy

  * mkdir ~/ proxy 
  * cd proxy 

用以下命令生成pac文件

  * genpac &#8211;proxy=&#8221;SOCKS5 127.0.0.1:1080&#8243; &#8211;gfwlist-proxy=&#8221;SOCKS5 127.0.0.1:1080&#8243; -o autoproxy.pac &#8211;gfwlist-url=&#8221;<https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt>&#8220;

3、设置全局代理 点击：System settings > Network > Network Proxy，选择 Method 为 Automatic，设置 Configuration URL 为 autoproxy.pac 文件的路径，点击 Apply System Wide。 格式如：file:///home/{user}/ proxy /autoproxy.pac

使用共享的PAC规则文件进行上网(无效)

  * <https://raw.githubusercontent.com/clowwindy/gfwlist2pac/master/test/proxy_abp.pac>

使用SwitchyOmega 导出pac 然后有效

4.配置全局代理

为了让整个系统都走代理，需要配置全局代理，可以通过polipo实现。

首先是安装polipo：

  * sudo apt-get install polipo

接着修改polipo的配置文件/etc/polipo/config：

  * logSyslog = true
  * logFile = /var/log/polipo/polipo.log
  * proxyAddress = &#8220;0.0.0.0&#8221;
  * socksParentProxy = &#8220;127.0.0.1:1080&#8221;
  * socksProxyType = socks5
  * chunkHighMark = 50331648
  * objectHighMark = 16384
  * serverMaxSlots = 64
  * serverSlots = 16
  * serverSlots1 = 32

重启polipo服务：

  * sudo /etc/init.d/polipo restart

为终端配置http代理：

  * export http_proxy=&#8221;<http://127.0.0.1:8123/>&#8220;

接着测试下是否成功：

  * curl www.google.com

如果有响应，则全局代理配置成功。

4.注意事项

服务器重启后，下面语句需要重新执行：

export http_proxy=&#8221;<http://127.0.0.1:8123/>&#8220;