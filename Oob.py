#!/usr/bin/env python3
# -*- coding: utf-8 -*-

std1={'name':'mike','score':98}
std2 = {'name':'Tom','score':81}

def print_student(std):
    print('%s %d' % (std['name'],std['score']))

print(print_student(std1));
print(print_student(std2));


class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_student(self):
        print('%s %d' %(self.__name,self.__score))
    def getScore(self):
        return self.__score
    def setScore(self,score):
        self.__score = score

print( Student('txh',100).print_student());
s = Student('txh',100)
s.age = 20
print (s.age)
print(s)
#print(s.__name)
s.setScore(101)
print(s.getScore())
print(s._Student__name)
#new invarient
s.__name="t1"
print(s.print_student())


class Animal(object):
    def run(self):
        print("Animal is running")
class Dog(Animal):
    def run(self):
        print("dog is running")
class Cat(Animal):
    pass

print(Dog().run())
print(Cat().run())

class Timer(object):
    def run(self):
        print("time is running")

def runTwice(animal):
    animal.run()
    animal.run()

print(runTwice(Dog()))
print(runTwice(Timer()))


print(type(123))
print(type('str'))
print(type(abs))
print(type(s))

print(type(123) == int)
import types
print(type(lambda x:x) == types.LambdaType)
print(type(s) == Student)
print(type(Dog()))
print(isinstance(Dog(),Animal))
print(isinstance(Animal(),Dog))
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))
print(dir(s))
print(hasattr(s,'age'))
print(getattr(s,'age',10))



class Test(object):
    def __init__(self,test):
        self.test = test
    test = "test"
t = Test('123')
print(t.test)
t.test='456'
print(t.test)
del t.test
print(t.test)
