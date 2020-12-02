---
layout:        post
title:         "C++中的reference_wrapper用法"
date:          "2020-12-02 22:20:04 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - C++
---

## 背景 ##

在代码中需要创建一个std::map<std::string, int>的对象，由于这个std::string对象已经存在于std::list<std::string>中,所以在map里再维护一份会很浪费内存，于是使用了C++11中的std::ref来实现这个功能。

## std::ref的用法 ##

```
#include <iostream>
#include <functional>
using namespace std;

void printRef(std::string& s)
{
    cout << s << endl;
}


int main()
{
    string s1 = "s1";
    printRef(std::ref(s1));
    return 0;
}
```

std::ref会返回一个reference_wrapper对象，reference_wrapper能直接传给一个需要引用的形参，所以最简单的用法可以直接当做引用使用。


## std::reference_wrapper的用法 ##

```
#include <iostream>
#include <functional>
using namespace std;

int main()
{
    string s1 = "s1";
    reference_wrapper<string> sref = ref(s1);
    cout << sref.get() << endl;
    return 0;
}
```

reference_wrapper对象和智能指针用法类似，用get方法就可以获取出原本的引用对象。

## std::map结合std::reference_wrapper使用 ##

```
#include <iostream>
#include <map>
#include <functional>
using namespace std;

int main()
{
    map<reference_wrapper<const string>, int, less<const string&>> m;
    string s1 = "s1", s2 = s1;
    m.insert(make_pair(cref(s1), 1));
    auto it = m.find(s2);
    cout << "key is " << it->first.get() << ",value is "<< it->second << endl;
    return 0;
}
```

由于reference_wrapper做key的时候无法进行大小比较，所以map模板的第三个参数传入了对string引用的less对象来作为比较的方法。<br>
cref是对于const对象的包装，其余用法和ref一样。

## 参考文章 ##

[https://en.cppreference.com/w/cpp/utility/functional/ref](https://en.cppreference.com/w/cpp/utility/functional/ref)<br>
[https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper](https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper)<br>
[https://en.cppreference.com/w/cpp/container/map](https://en.cppreference.com/w/cpp/container/map)<br>
[https://stackoverflow.com/questions/3235927/reference-as-key-in-stdmap](https://stackoverflow.com/questions/3235927/reference-as-key-in-stdmap)