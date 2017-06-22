
class Student(object):
    pass
    __slots__ = ('setAdd','age','_score','_birth')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if  not isinstance(value,int):
            raise ValueError('Error must be an integerate')
        if value < 0 and value > 100:
            raise ValueError('score must between 0~100')
        self._score = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def old(self):
        return 2017 - self._birth

def setAdd(self,age):
    self.age = age

s = Student()
from types import MethodType

s.setAdd = MethodType(setAdd,s)
s.setAdd(25)
print(s.age)

Student.setAdd = setAdd
s1 = Student()
s1.setAdd(25)
print(s1.age)
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

s1.score = 100
print(s1.score)

s1.birth = 2000
print(s1.old)



class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Flyable(object):
    def fly(self):
        print('flying...')

class Runable(object):
    def run(self):
        print('running...')

class Dog(Mammal,Runable):
    pass

class Parrot(Bird,Flyable):
    pass


class Student_1(object):
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Student Object (name,%s)'%self._name
    __repr__ = __str__

print(Student_1('txh'))
s1 = Student_1('txh')
print(s1)


class Fib(object):
    def __init__(self):
        self._a = 0
        self._b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self._a,self._b = self._b,self._a+self._b
        if self._a > 10000:
            raise StopIteration()
        return self._a

    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for i in range(n):
                a,b = b, a + b
            return a
        if isinstance(n,slice):
            s = n.start
            e = n.stop
            if s is None:
                s = 0
            L = []
            a,b = 1,1
            for i in range(e):
                if i >= s:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, item):
        if  item == 'name':
            return 'fib'
        elif item == 'func':
            return lambda: 25
        raise AttributeError('Fib has not attribution member')

    def __call__(self, *args, **kwargs):
        return 'I have a fib func'


# for i in Fib():
#     print(i)
#

print('-------------------------------------------')
print(Fib()[1:10])
print(Fib().name)
print(Fib().func())
print(Fib()())
print(callable(Fib))


from enum import Enum
Month = Enum('month',('Jan','Feb','Match'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4

print(Weekday.Sun.value)


class Hello(object):
    def hello(self,name = 'world'):
        print('hello,%s'%name)

print(type(Hello))
print(type(Hello()))

def helloType(self,name = 'world'):
    print('hello,%s'%name)

HelloType = type('HelloType',(object,),dict(fn = helloType))
HelloType().fn('type')