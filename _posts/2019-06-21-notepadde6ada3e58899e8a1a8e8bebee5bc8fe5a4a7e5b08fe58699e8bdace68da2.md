---
id: 256
title: notepadd++正则表达式大小写转换
date: 2019-06-21T14:27:23+08:00
author: Remilia Scarlet
layout: post
tags:
  - 正则表达式
---
<blockquote class="wp-block-quote">
  <p>
    示例1：将语句 test this sentence 转为大写
  </p>
  
  <p>
    查找：^.*$
  </p>
  
  <p>
    替换：\U$0
  </p>
  
  <p>
    或&#8212;&#8212;&#8212;&#8212;
  </p>
  
  <p>
    查找：^(.*)$
  </p>
  
  <p>
    替换：\U\1 或 \U$1
  </p>
</blockquote>

<blockquote class="wp-block-quote">
  <p>
    示例2：将语句 TEST THIS SENTENCE 转为小写
  </p>
  
  <p>
    查找：^.*$
  </p>
  
  <p>
    替换：\L$0
  </p>
  
  <p>
    或&#8212;&#8212;&#8212;&#8212;
  </p>
  
  <p>
    查找：^(.*)$
  </p>
  
  <p>
    替换：\L\1 或 \L$1
  </p>
</blockquote>

<blockquote class="wp-block-quote">
  <p>
    示例3：将语句 test this sentence 首字t母转为大写
  </p>
  
  <p>
    查找：^.
  </p>
  
  <p>
    替换：\U$0
  </p>
  
  <p>
    或&#8212;&#8212;&#8212;&#8212;
  </p>
  
  <p>
    查找：^(.)
  </p>
  
  <p>
    替换：\U\1 或 \U$1
  </p>
</blockquote>

<blockquote class="wp-block-quote">
  <p>
    示例4：将语句 Test this sentence 首字T母转为小写
  </p>
  
  <p>
    查找：^.
  </p>
  
  <p>
    替换：\L$0
  </p>
  
  <p>
    或&#8212;&#8212;&#8212;&#8212;
  </p>
  
  <p>
    查找：^(.)
  </p>
  
  <p>
    替换：\L\1 或 \L$1
  </p>
</blockquote>

<blockquote class="wp-block-quote">
  <p>
    示例5：将语句 test this sentence 每个单词首字母转为小写
  </p>
  
  <p>
    查找：\b(\w)(\w*)\b
  </p>
  
  <p>
    替换：\U$1\E$2 或 \U\1\E\2
  </p>
</blockquote>

<blockquote class="wp-block-quote">
  <p>
    总结：
  </p>
  
  <p>
    1、\U 将匹配项转为大写(Upper)&nbsp;<br />2、\L 将匹配项转为小写(Lower)&nbsp;<br />3、\E 终止转换(End)
  </p>
</blockquote>