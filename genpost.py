#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import time
import string
import re

cf = {
    'author':'Remilia Scarlet',
    'header-img': "img/post-bg-2015.jpg"
}

def menuSelect(s,l):
    print(s)
    for i in range(0, len(l)):
        print('\t%d) %s' % (i+1,l[i]))
    i = input("layout:")
    if i == '':
        return l.index('post')
    return int(i)-1

def inputTags(s):
    tags = input(s)
    tags = [i.strip() for i in tags.split(',')]
    s = '    - '
    tmp=''
    for i in tags:
        if i != '':
            tmp+=s+i+'\n'
    return tmp.rstrip('\n')

def checkTitle(s):
    for i in s:
        if i not in''.join((string.ascii_letters,string.digits,'_',' ')):
            return False
    return True

def getYaml(cf):
    def getLine(s):
        return '%-15s%s\n' % (s+':',cf[s])
    def getLineWithQuoto(s):
        if cf[s] == '':
            return cf[s]
        return '%-15s"%s"\n' % (s+':',cf[s])
    yaml = '''---\n%s%s%s%s%s%stags:\n%s\n---\n''' \
           % (getLine('layout'), getLineWithQuoto('title'), getLineWithQuoto('subtitle'), getLineWithQuoto('date'), getLineWithQuoto('author'),getLineWithQuoto('header-img'), cf['tags'])
    return yaml


if __name__ == '__main__':
    layouts = [os.path.splitext(i)[0] for i in os.listdir('_layouts')]
    cf['layout'] = layouts[menuSelect('What layout do you want to use?(default is post)',layouts)]
    cf['title'] = input("input title:")
    #while cf['title'] == '' or not checkTitle(cf['title']):#中文名也是可行的，只是在windows上有bug而已
    #    print('Title should be in English!')
    #    cf['title'] = input("input title again:")
    cf['subtitle'] = input('input subtitle:')
    cf['tags'] = inputTags('input tags(split by comma):')
    cf['date'] = time.strftime("%Y-%m-%d %H:%M:%S +0800", time.localtime())
    filename = time.strftime("%Y-%m-%d", time.localtime())+'-%s' % re.sub(r'\-+' , '-', re.sub(r'[?*\/<>:"|]','-', cf['title'])) #cf['title'].replace(' ','-')
    #yaml ='''---\nlayout:     %s\ntitle:      "%s"\nsubtitle:   "%s"\ndate:       %s\nauthor:     "%s"\nheader-img: "img/post-bg-2015.jpg"\ntags:\n%s\n---\n''' \
    #       % (layout,title,subtitle,date,author,tags)
    yaml = getYaml(cf)
    path = '_posts'
    if os.path.exists(path):
        with open('%s/%s.markdown'% (path,filename),'w',encoding='utf-8') as f:
            f.write(yaml)
