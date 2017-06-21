
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score= score
    def printInfo(self):
        print("%s %s"%(self.__name,self.__score))

s1 = Student('txh',100)
s1.printInfo()
# s1._Student__name
s1.test = 'test'
print(s1.test)
print(Student)

class Animal(object):
    def run(self):
        print('animal is running')

class Dog(Animal):
    pass
    def eat(self):
        print('eating something')
    def run(self):
        print('dog is running')

t = Dog()
t.run()
t.eat()

print(isinstance(t,Animal))
print((isinstance(t,Dog)))

def runTwice(Animal):
    Animal.run()
    Animal.run()

runTwice(Animal())
runTwice(Dog())

class Timer():
    def run(self):
        print('Time is running')
runTwice(Timer())

print(type('asd'))
print(type(abs))
print(type(t))
print(type(t.run))
print(type(type(t)))

import types
print(type(abs) == types.BuiltinFunctionType)
#类使用isinstance来判断

print(dir(t))

class testLen(object):
    def __len__(self):
        return 100
print(len(testLen()))

class funcTest(object):
    Name = 'student'
print(funcTest.Name)
funcTest().Name = 'Student'
print(funcTest().Name)