---
layout:        post
title:         "Post html with jekyll"
subtitle:      "在jekyll框架里直接发布静态html页面"
date:          "2020-04-24 10:28:21 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - jekyll
    - html
    - js
---

# 发现 #
今天发现在jekyll构建的git pages不仅支持markdown格式，也能直接发布html格式。特此写一篇文章记录过程。

# 过程 #
## 1.创建html文件 ##
直接在_post/文件夹中创建文件，格式为year-month-date-you-title.html(和markdown的一样，区别在于后缀)

然后直接编写html内容即可。

## 2.其他文件位置 ##
js文件直接放在js/下，css文件放在css/文件下,图像文件放在img/下

引用时直接使用绝对路径,例如/js/soumao.js


# 样例 #
(转载自[https://github.com/tcdw/servalclock](https://github.com/tcdw/servalclock))

[薮猫报时器](/2020/04/24/sou-mao/)
