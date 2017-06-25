from datetime import datetime,timedelta,timezone

now = datetime.now()
print(now)
print(type(now))

now = datetime(2017,6,25)
print(now)
print(now.timestamp())

print(now.fromtimestamp(now.timestamp()))
print(now.utcfromtimestamp(now.timestamp()))


# str to datetime
cday = datetime.strptime('2017-6-25','%Y-%m-%d')
print(cday)
print(type(cday))

# datetime to str
sday = now.strftime('%Y-%m-%d %H:%M:%S')
print(sday)
print(type(sday))

print(now+timedelta(hours=10))


from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('%d %d'%(p.x,p.y))
print(isinstance(p,Point))
print(isinstance(p,tuple))

from collections import deque
q = deque(['t','x','h'])
q.append('6')
q.appendleft('5')
print(q)
q.pop()
q.popleft()
print(q)


from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
for k,v in d.items():
    print(k,v)

d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for k,v in d.items():
    print(k,v)


from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)


import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))