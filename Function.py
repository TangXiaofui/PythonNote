n1 = 255
n2 = 1000
print("255 = %s"%hex(n1))
print(hex(n2))

def myAbs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if  x >= 0:
        return x
    else:
        return -x

print(myAbs(-10))
def nop():
    pass
import math

def move(x,y,step,angle):
    xpos = x + step * math.cos(angle)
    ypos = y + step * math.sin(angle)
    return xpos,ypos

print(move(0,0,10,math.pi/6))

def quardratic(a,b,c):
    L = [a,b,c]
    for l in L:
        if  not isinstance(l,(int,float)):
            raise TypeError("bad operand type")

    if a == 0:
        if b != 0:
            return -c/b
        else:
            return 'error'
    else:
        D = b**2 - 4 * a * c
        if D >= 0 :
            s1 = (-b + math.sqrt(D))/(2 * a)
            s2 = (-b - math.sqrt(D))/(2 * a)
            return (s1,s2)
        else:
            return 'error'

print(quardratic(2,3,1))
print(quardratic(1,3,-4))


def myPower(x,n = 2):
    sum = 1
    while n:
        n = n - 1
        sum = sum * x
    return sum

print(myPower(3,4))
print(myPower(3))


def enroll(name,gender,age = 20,city = 'guangzhou'):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city",city)

print(enroll("txh","boy"))

print(enroll('txh','boy',city='jinjiang'))


def add_end(L = []):
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end())
print(add_end())


def add_end_1(L=None):
    if  L == None:
        L = []
    L.append('end')
    return L
print(add_end_1())
print(add_end_1())

# ，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def calcuNum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(calcuNum([1,2,3,4,5]))

def calcuNum2(*number):
    s = 0
    for n in number:
        s = s + n * n
    return s
print(calcuNum2(1,2,3))
print(calcuNum2(2,3,4,5,6))

L = [1,2,3,4,5,6]
print(calcuNum2(*L))

def person(name,age,**kw):
    print("name",name)
    print("age",age)
    if 'city' in kw:
        print("welcome")
    print("other",kw)

print(person("txh",20))
print(person("txh",20,city = "jinjiang",gender = "boy"))

extra = { "gender" : "boy","city" : "jinjiang"}
print(person("txh",21,**extra))


def person2(name,age,*,gender,city):
    print("name",name,"age",age,gender,city)
print(person2("txh",20,**extra))


print("------------------------------------------------------")
def person3(name,age,*args,gender,city):
    print("name",name,"age",age,args,gender,city)
print(person3("txh",20,[1,2,3],**extra))


def person4(name,age = 20,*args,gender,city = "guangzhou",**kw):
    print(name,age,args,gender,city,kw)

print(person4("txh",gender="boy",sport = "basketball"))


def hello(greeting,*name):
    if  len(name) == 0:
        print("%s! " % greeting )
    else:
        print("%s,%s!" %(greeting,','.join(name)))

print("hello","txh","txh","txh")


def print_score(**kw):
    print('     name    score')
    print('------------------')
    for name,score in kw.items():
        print('%10s    %d ' % (name,score))
    print()

print_score(t=100,x=10,h=00)


def fact(n):
    if  n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

def HanataMove(n,a,b,c):
    if  n == 1:
        print('move:%s -> %s'%(a,c))
    else:
        HanataMove(n-1,a,c,b)
        HanataMove(1,a,b,c)
        HanataMove(n-1,b,a,c)

print(HanataMove(4,'a','b','c'))