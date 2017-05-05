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
