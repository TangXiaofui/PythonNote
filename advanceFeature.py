L = ['t','x','h','2','0','1','7']
print(L[:3])
print(L[-4:])

L = list(range(100))
print(L[10:20])
print(L[:10:2])

d = {'a':1,'b':2, 'c':3 }
for x in d:
    print(x)

for x in d.values():
    print(x)


from collections import Iterable
print( isinstance('aa',Iterable))
print(isinstance([1,2,3,4],Iterable))
print(isinstance(123,Iterable))

print(L[0])

for i,value in enumerate(['A','B','C']):
    print(i,value)

print([x*x for x in range(1,11) if x % 2 == 0])

print([m+n for m in ['a','b','c'] for n in ['A','B','C']])

import os
print([d for d in os.listdir('.')])

d = {'a':'A','b':'B'}
print([key+ '='+ value for key,value in d.items()])

print([value.lower() for value in d.values()])

g = (x * x for x in range(1,10))
for v in g:
    print(v)


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

for v in fib(6):
    print(v)


def step():
    print('step 1')
    yield 1;
    print('step 2')
    yield 2
    print('step 3')
    yield 3

for s in step():
    print(s)

def triangles(n):
    L = [1]
    i = 1
    while i < n:
        L = [1] + [ L[x-1]+ L[x] for x in range(1,len(L))] + [1]
        yield L


g = triangles(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

from collections import Iterator,Iterable
print(isinstance('abc',Iterable))
print(isinstance('abc',Iterator))
print(isinstance(iter('abc'),Iterator))


