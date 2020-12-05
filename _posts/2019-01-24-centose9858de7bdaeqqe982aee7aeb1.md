---
id: 14
title: CentOS配置QQ邮箱
date: 2019-01-24T13:36:43+08:00
author: Remilia Scarlet
layout: post
tags:
  - Linux运维
---
 

**1.安装mailx**

yum -y **install** mailx 



**2.编辑配置文件**

vim /etc/mail.rc 在文件末尾添加  

<pre class="wp-block-code"><code>set nss-config-dir=/root/.cert
set ssl-verify=ignore
set smtp="smtps://smtp.qq.com:465" #第二个博客写的地址不对
set smtp-auth=login
set smtp-auth-user="zh616110538@qq.com"
set smtp-auth-password="qq邮箱授权密码" #（在QQ邮箱 设置-账户- POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务 里寻找）
set from="zh616110538@qq.com"</code></pre>

**3.生成证书**

<pre class="wp-block-code"><code>mkdir -p /root/.certs/
echo -n | openssl s_client -connect smtp.qq.com:465 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ~/.certs/qq.crt
certutil -A -n "GeoTrust SSL CA" -t "C,," -d ~/.certs -i ~/.certs/qq.crt
certutil -A -n "GeoTrust Global CA" -t "C,," -d ~/.certs -i ~/.certs/qq.crt
certutil -L -d /root/.certs
</code></pre>

**4.确认证书**

<pre class="wp-block-code"><code>cd /root/.certs
certutil -A -n "GeoTrust SSL CA - G3" -t "Pu,Pu,Pu"  -d ./ -i qq.crt</code></pre>

**5.测试是否成功**

echo &#8220;test&#8221; |mail -s &#8220;test&#8221; [zh616110538@qq.com](mailto:zh616110538@gmail.com)