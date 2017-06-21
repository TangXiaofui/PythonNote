'a test module'

__authon__ = 'txh'

import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s'%args)
    else:
        print('too many arguent')

def _private_1(name):
    return 'hello %s' % name
def __private_2(name):
    return 'hi %s' % name

def greeting(name):
    if len(name) > 3 :
        print(_private_1(name))
    else:
        print(__private_2(name))

from PIL import Image
im = Image.open('thumb.jpg')
print(im.format,im.size,im.mode)
print(sys.path)

if __name__ == '__main__':
    test()
    greeting('txh')
    greeting('aaaaaaaaaa')
