#!/usr/bin/env python3
# *-* coding: utf-8 *-*

L = ['a','b','c','d','e']
l = []
n = 3
for i in range (n):
    l.append(L[i])

print(l)   
print(L[0:3])
print(L[:3])
print(L[-2:])

L=list(range(100))

print(L[:10:2])
print(L[::5])
print((1,2,3,4,5)[:3])

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for v in d.values():
    print(v)

for i,name in enumerate(['a','b','c']):
    print(i,name)

for x,y in [(1,1),(2,4),(3,9)]:
    print ( x,y)


print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2 == 0])

print([m+n for m in 'abc' for n in 'ABC'])

import os
print ([ d for d in os.listdir('.')])


for k,v in d.items():
    print(k,'=',v)
d = {'e':'A','f':'B'}
print([k + '=' + v for k,v in d.items()])

print([s.lower() for s in d.values()])



L=[x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print (next(g))

for n in g:
    print(n)


def fib(n):
    i,a,b = 0,0,1
    while i < n :
        yield b
        a,b = b,a+b
        i += 1
    return "done"
print(fib(2))


def odd():
    print ('stage1')
    yield 1
    print ('stage2')
    yield 2
    print ('stage3')
    yield 3

print ( next(odd()))
print ( next(odd()))

o = odd();
next(o);
next(o);
next(o);

f = fib(6)

#for i in f:
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print("generator retun value:",e.value)
        break



def Triangle():
    L=[1]
    for i in range(10):
        yield L
        L = [1] + [ L[j] + L[j+1] for j in range(len(L)-1)] + [1]
for i in Triangle():
    print (i)

print(next(Triangle()))

from collections import Iterable
from collections import Iterator
print( isinstance([],Iterable) )
print( isinstance({},Iterable) )
print( isinstance(Triangle(),Iterator) )

