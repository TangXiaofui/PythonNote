
class Student(object):
    pass
    __slots__ = ('setAdd','age')

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