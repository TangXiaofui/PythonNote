#!/usr/bin/env python3
# *-* coding: utf-8 *-*

def add(x,y,f):
    return f(x)+f(y)

print(add(-6,5,abs))

def func(x):
    return x * x


r = map(func,[i for i in range(1,10)])
print (list(r))

r = map(str,[i for i in range(1,10)])
print (list(r))


from functools import reduce

def str2int(s):
#    def fn(x,y):
#        return x * 10 + y
    def char2num(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
#    return reduce(fn,map(char2num,s))
    return reduce(lambda x,y: x * 10 + y,map(char2num,s))
print(str2int('13579'))


def is_odd(n):
    return n%2 == 1

def FilterOdd(l):
    return filter(is_odd,l)
print(list (FilterOdd([i for i in range(1,10)])) )


def not_empty(s):
    return s and s.strip()

print( list( filter(not_empty,['A','B',' C  ',None,'  ']) ) )


def isParlindrome(n):
    s = str(n)
    return s == s[::-1]
output = filter(isParlindrome,range(1,10000))
print (list(output))

L=[36,6,-12,9,-21]
print(sorted(L))
print(sorted(L,key = abs))

L=['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L,key = str.lower))
print(sorted(L,key = str.lower,reverse=True))


def lazy_sum(*args):
    def sum():
        total = 0
        for i in args:
            total += i
        return total
    return sum

sum1 = lazy_sum(1,2,3,4)
sum2 = lazy_sum(1,2,3,4)
print (sum1 == sum2)
print (sum1())


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3= count()
print(f1())
print(f2())
print(f3())


def count2():
    fs = []
    def f(i):
        def g():
            return i*i
        return g
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3= count2()
print(f1())
print(f2())
print(f3())


m1 = map(lambda x:x*x ,[1,2,3,4,5,6,7,8])
f1 = lambda x:x*x
print (list(m1))
print (f1(5))

import functools


def log(text):
    def deractor(func):
        @functools.wraps(func)
        def Wrapper(*args,**kw):
            print("%s %s"%(text,func.__name__))
            return func(*args,**kw)
        return Wrapper
    return deractor

#@log('execute')
def now():
    print("2017-5-8")
now = log('execute')(now)
print(now())
print(now.__name__)


def int2(x,base=2):
    return int(x,base)
def int16(x,base=16):
    return int(x,base)
print (int2('10101010'))
print (int16('0x10'))


int8=functools.partial(int,base=8)
print(int8('010'))
