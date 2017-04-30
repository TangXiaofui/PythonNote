#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def area_of_circle(r):
    pi = 3.14
    return pi * r ** 2

def sum2(start,end,func):
    total = 0;
    for x in range(start,end):
        total += func(x)
    return total

def func1(x):
    return x

def func2(x):
    return x**2 + 1

def nop():
    pass

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if (x >= 0):
        return x
    elif (x < 0):
        return -x

print (area_of_circle(2))
print (sum2(1,4,func2))
print (nop())

import math
def move(x,y,step,angle = 0):
    xn = x + step * math.cos(angle)
    yn = y + step * math.sin(angle)
    return xn,yn

x,y = move(10,10,10,math.pi/6)
print (x,y)

#return tuple
r = move (100,100,100,math.pi/6)
print (r)

def quadratic(a,b,c):
    L = [a,b,c]
    for x in L:
        if not isinstance(x,(int,float)):
            raise TypeError("bad Type")

    if(a == 0):
        if(b != 0):
            return -c/b
        else:
            print ("无解")
    else:
        D = b**2 - 4 * a * c
        if(D >= 0):
            x1 = (-b+math.sqrt(D))/(2 * a)
            x2 = (-b-math.sqrt(D))/(2 * a)
            return x1,x2
        else:
            print('无解')

print (quadratic(2,3,1))


def enroll(name,gender,age=6,city = "bejing"):
    print ("name : %s"%(name))
    print ("gender :",gender)
    print ('age :',age)
    print ('city :',city)
enroll('xxx','boy')
enroll('txh','boy',city='jinjiang')


#def add_end(L=[]):
#    L.append('END')
#    return L
def add_end(L = None):
    if( L == None):
        L = []
    L.append('END')
    return L
print (add_end())
print (add_end())


def calc(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

print(calc(1,2,3))
print(calc(1,2))

num = [1,2,3,4,5]
print(calc(*num))

def person(name,age, **kv):
    if('job' in kv):
        pass
    print('name',name,'age',age,'other',kv)

print ( person('txh',20,city='jinjiang') )
extra = {'city':'jinjiang','job':'student'}
print ( person('txh',20,city=extra['city']) )
print ( person('txh',20, **extra))

def person2(name,*,age=20):
    print(name,age)

#print( person2('txh',20))
print( person2('txh',age=20))
print( person2('txh'))

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print (f1(1,2,d=3,y=4))
print (f2(1,2,d=3,y=4))
print (f1(1,2,3,'a','b',y=4))

args=(1,2,3)
kw={'d':99}
print(f1(*args,**kw))
print(f2(*args,**kw))
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。

def fact(x):
    if(x == 1):
        return 1
    return x * fact(x-1)

def fact2(x):
    return fact_iter(x,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
print (fact(5))
print (fact2(5))

def move(n,a,b,c):
    if(n == 1):
        print(a+'->'+c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

print(move(3,'a','b','c'))
