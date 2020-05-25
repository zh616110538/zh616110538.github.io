---
layout:        post
title:         "利用docker搭建美化过的nginx目录站"
date:          "2020-05-25 15:19:35 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - nginx
    - docker
---

## 1.拉取docker镜像 ##
    docker pull fraoustin/fancyindex

## 2.拉取美化的fancy主题 ##
    git clone https://github.com/Naereen/Nginx-Fancyindex-Theme

## 3.修改nginx配置文件 ##
创建default.conf文件，作为主配置文件

<pre>root@update:/etc/nginx/conf.d# cat default.conf
server {
    listen 80 default_server;
    client_max_body_size 1G;

    charset utf-8,gbk;
    location /Nginx-Fancyindex-Theme-light{
       rewrite /Nginx-Fancyindex-Theme-light/(.*) /$1  break;
       root /theme/Nginx-Fancyindex-Theme1/Nginx-Fancyindex-Theme-light;
   }

    root /share;
    location / {
        # manage DELETE AND MKDIR
        if (-d $request_filename) { rewrite ^(.*[^/])$ $1/ break; }

        root /share;
        include /theme/Nginx-Fancyindex-Theme1/fancyindex.conf;
    }
}
</pre>

## 4.启动docker容器 ##
    docker run --restart=always -p 80:80 -v /home/www/html:/share -v /usr/share/nginx/Nginx-Fancyindex-Theme/:/theme/Nginx-Fancyindex-Theme1 -v /etc/nginx/conf.d:/etc/nginx/conf.d -d --name nginx fraoustin/fancyindex

/home/www/html是你站点的根目录<br>
/usr/share/nginx/Nginx-Fancyindex-Theme是第二步拉下来的主题<br>
/etc/nginx/conf.d是第三步创建的default.conf所在的文件夹

## 参考链接 ##
[https://segmentfault.com/a/1190000012606305](https://segmentfault.com/a/1190000012606305)<br>
[https://hub.docker.com/r/fraoustin/fancyindex](https://hub.docker.com/r/fraoustin/fancyindex)<br>
[https://github.com/Naereen/Nginx-Fancyindex-Theme](https://github.com/Naereen/Nginx-Fancyindex-Theme)