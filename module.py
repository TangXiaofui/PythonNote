#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'
__author__ = 'txh'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print ("hello,world")
    elif len(args) == 2:
        print ("hello,%s"%args[1])
    else:
        print("too many args")

def _private1(name):
    return 'hello,%s'%name
def _private2(name):
    return 'hi,%s'%name

def greeting(name):
    if( len(name) > 3):
        return _private1(name)
    else:
        return _private2(name)  

#sudo pip3 install Pillow
import sys
from PIL import Image
im = Image.open('ascii-unicode-utf-8.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','jpeg')
print(sys.path)

if __name__ == '__main__':
    test()
    print ( greeting('txh'))
    print ( greeting('tangxiaohui'))
