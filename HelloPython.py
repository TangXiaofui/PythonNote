
print(100+200+300)
print("hello python")

#print val
a = 100
if a > 0:
    print (a)
else:
    print(-a)
    
b = 1.234567890
print (b)

print ("I'm OK")
print ("I'm \"OK\"  ")

print ('\\\r\\ ')
print (r'\\\r\\')
print ('''line1
line2
line3''')

print (5 > 3 and 1 > 2)
print (5 > 3 or 1 > 2)
print (not 5)

print(a)
a = 'abc'
print (a)

x=10
x = x+2
print (x)

b = a
a = 'def'
print(b)

print( 10 / 3)
print(10 // 3)
print( 10%3 )

print('''n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = 'Hello,"Bart"'
s4 = r\'''Hello,
Lisa!\'\'\''''
)

print (ord('A'))
print (ord('中'))
print (chr(66))
print (chr(25991))

print (b'abc')
print ('abc'.encode('ascii'))
print ('abc')
print ('中文'.encode('utf-8'))
print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


print (len(b'abc'))
print (len('中文'))
print (len('中文'.encode('utf-8')))


print ('hello %s , you have $%d.'%('txh',10000))
print ('%2d-%02d'%(1,2))
print ('%.2f' %3.1415)
print ('%d%%'%7)

#list []
classmate = ['t','x','h']
print (classmate)
print (len(classmate))
print (classmate[0])
print (classmate[-1])
classmate.append('e')
classmate.insert(0,'b')
print (classmate)
classmate.pop()
classmate.pop(0)
print (classmate)
classmate[0] = 'T'
print (classmate)
L = ['123',123,False]
S = ['txt',123,L,True]
print (S)

#tuple () const
classmate = ('t','x','h')
t = (1)
t2 = (1,)
print (t)
print (t2)
#指向不变，但是指向的可以变
t3 = ('a','b',['x','y'])
t3[2].append('z')
print (t3)

x = 20
if x > 18:
    print ('test')
    print ('adult')
elif x > 6:
    print ('teenager')
else:
    print ('kid')
# if + and or
s = input("birth : ")
b = int(s)
if b < 2000:
    print ('00前')
else:
    print ('00后')


for c in classmate:
    print (c)

sum = 0
for i in [1,2,3,4,5,6,7,8,9]:
    sum = sum+i
print (sum)

sum = 0
for i in range(10):
    sum = sum + i
print(sum)

n = 99
sum = 0
while n > 0:
    sum = sum +n
    n = n-2
print (sum)


n = 0
while n < 100:
    if(n >= 10):
        break
    print(n)
    n = n+1
print ('END')


n = 0
while (n < 10):
    n = n+1
    if(n % 2 == 0):
        continue
    print (n)
print ('END')


#dict 空间换时间 key对象不能变,即类似list不能用作key
d = {'t':95,'x':90}
print (d)
d['h'] = 99
print (d)
print ('h' in d)
print (d.get('1',-1))
d.pop('h')
print (d)

#set
s = set([1,1,2,2,3,3])
print (s)
s.add(4)
print (s)
s.remove(4)
print (s)
s.add((1,2,3))
print (s)
#s.add((1,2,[2,3]))


s1 = set([1,2,3])
s2 = set([2,3,4])
print (s1 & s2)
print (s1 | s2)


s = ['c','b','a']
s.sort()
print (s)

a = 'abc'
b = a.replace('a','A')
print(b)
print(a)

