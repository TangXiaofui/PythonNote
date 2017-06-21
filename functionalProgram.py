f = abs
print(f(-10))

def add1(a,b,f):
    return f(a)+f(b)
print(add1(2,-2,abs))

def func1(x):
    return x*x

print(list( map(func1,[1,2,3,4,5])))

from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5]))

def fn(x,y):
    return x*10+y
def charToint(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]

print(reduce(fn,map(charToint,'13579')))

def strToint(s):
    def fn(x,y):
        return x * 10 + y
    def charToint(x):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
    return reduce(fn,map(charToint,s))

print(strToint('12345'))

print(reduce(lambda x,y:x*10+y,map(charToint,'14567')))


def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = map(normalize,L1)
print(list(L2))

from operator import mul
def prod(num):
    return reduce(mul,num)
print(prod([1,3,5,7]))


def isOdd(x):
    return x % 2 ==0

print(list(filter(isOdd,[1,2,3,4,5,6,7])))

print(sorted([-3,1,5,-9]))
print(sorted([-3,1,5,-9],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

def lazySum(*num):
    def Sum():
        s = 0
        for i in num:
            s = s+i
        return s
    return Sum

# f = lazySum(*[1,3,5,7,9])
f = lazySum(1,3,5,7,9)
print(f())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())

def count1():
    fs = []
    def f(x):
        def g():
            return x*x
        return g
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

print(count.__name__)


def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper



import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' %(text,func.__name__) )
            return func(*args,**kw)
        return wrapper
    return decorator

@log('abc')
def now():
    print('2017-6-21')

now()
print(now.__name__)

print(int('1234',base=8))

def int2(x):
    return int(x,base=2)
print(int2('1111'))

int16 = functools.partial(int,base = 16)
print(int16('0xf'))