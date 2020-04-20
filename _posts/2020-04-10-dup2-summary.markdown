---
layout:        post
title:         "dup2 summary"
subtitle:      "linux里使用dup2的一些总结"
date:          "2020-04-10 17:20:20 +0800"
author:        "Remilia Scarlet"
header-img:    "img/post-bg-2015.jpg"
tags:
    - linux
    - c
---

# dup2的作用 #
参考手册[https://linux.die.net/man/2/dup2](https://linux.die.net/man/2/dup2)

用第一个文件描述符替换掉第二个（相当于关闭第二个文件描述符，然后进行数字上的替换）

# 示例代码 #



    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <assert.h>
    #include <fcntl.h>
    #include <sys/wait.h>
    
    int main(int argc,char **argv)
    {
            int ret = fork();
            assert(ret > -1);
            if(ret == 0){ //child
                    int fd = open("output",O_CREAT | O_TRUNC | O_RDWR,0644);
                    assert(fd > -1);
                    fd = dup2(fd,STDOUT_FILENO);
                    char *myargv[] = {"echo", "executed by execv",NULL};
                    execv("/bin/echo",myargv);
            }
            else{ //parent
                    int ls = wait(NULL);
            }
            return 0;
    }

# 示例解释 #
首先fork了一个子进程，然后主进程等待子进程完成。子进程此时打开了一个新的文件，并用dup2函数替换掉了标准输出的文件描述符，随后调用exec时新的进程用的文件描述符也是保持当前状态，最后将内容输出时实际上会输出到output文件中。