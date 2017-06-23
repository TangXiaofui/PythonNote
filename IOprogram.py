
# fd = open('./notfound.txt','r')
try:
    fd = open('./.gitignore','r')
    print(fd.read())
finally:
    if fd :
        fd.close()

with open('./.gitignore','r') as f:
    print(f.read())


with open('.gitignore','r') as f:
    for x in f.readlines():
        print(x.strip('\n'))

with open('thumb.jpg','rb') as f:
    for x in f.readlines():
        print(x)

# with open('testWrite.txt','w',encoding='gbk') as f:
#     f.write('中文')
#
# with open('testWrite.txt','r',encoding='utf-8') as f:
#     print(f.read())


from io import StringIO

mio = StringIO()
mio.write('hello')
mio.write(' ')
mio.write('txh')
print(mio.getvalue())

mio = StringIO('hello\nhi\ntxh')
while True:
    s = mio.readline()
    if  s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

import os
print(os.name)
print(os.environ)
print(os.path.abspath('.'))
print(os.path.join('.','testDir'))
# os.mkdir()
# os.rmdir()
print(os.path.split(os.path.abspath('.')))
print(os.path.splitext('./text.txt'))
# os.rename()
# os.remove()

import shutil
# shutil.copyfile()

print( [ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py' ] )

from datetime import datetime
pwd = os.path.abspath('.')

print('         Size    Last    Modified    Name')
print('-----------------------------------------')
for x in os.listdir(pwd):
    fsize = os.path.getsize(x)
    ftime = datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(x) else ''
    print('%10d %s %s %s'%(fsize,ftime,x,flag))


import pickle
d = dict(name = 'txh',age = 20, gender = 'boy')
print(pickle.dumps(d))

with open('testPickle.txt','wb') as f:
    pickle.dump(d,f)

with open('testPickle.txt','rb') as f:
    dd = pickle.load(f)
print(dd)

import json
print(json.dumps(d))
json_str ='{"age": 20, "score": 88, "name": "Bob"}'
py_str = json.loads(json_str)
print(py_str)

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

#
# def student2json(std):
#     return {'name':std.name,'age':std.age}

s = Student('txh',20)
# print(json.dumps(s,default=student2json))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'])
json_str = '{"name":"txh","age":20}'
print(json.loads(json_str,object_hook=dict2student))