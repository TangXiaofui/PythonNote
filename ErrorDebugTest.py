
def Error(x):
    try:
        print('try...')
        r = 10 / x
        print('result : %d'%r)
    except ValueError as e:
        print('Value error')
    except ZeroDivisionError as e:
        print('divide by zero')
    finally:
        print('finally...')

Error(10)
Error(0)


def foo(x):
    return 10 / x

def bar(x):
    return foo(x) * 2

def test():
    try:
        bar(0)
    except ZeroDivisionError as e:
        print('Zero Divide %s'%e)
    finally:
        print('finally...')

test()

import logging
def testLog():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

# testLog()

def foo1(x):
    n = int(x)
    if n == 0:
        raise ValueError('invalid value %s'%x)
    return 10 / x
def testRaise():
    try:
        foo1(0)
    except ValueError as e:
        print('value error')
        raise

# testRaise()

def foo2(x):
    i = int(x)
    assert i != 0, 'zero'

# print(foo2('0'))

import logging
logging.basicConfig(level=logging.INFO)
import pdb

s = '0'
n = int(s)
logging.info('n = %d' % n)
# pdb.set_trace()
# print(10 / n)


class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('no has key')

    def __setattr__(self, key, value):
        self[key] = value

# import unittest
# class TestDict(unittest.TestCase):
#     def test_Init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,Dict))
#
#     def test_Key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key,'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
if __name__ == '__main__':
    # unittest.main()
    import doctest
    doctest.testmod()