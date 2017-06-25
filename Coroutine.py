
def comsume():
    r = ''
    print('aaaaaaaaaaaa')
    while True:
        n = yield r
        if not n:
            return
        r = 'txh'
        print('Comsuming...%s'%n)
    print('done')

def product(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('Product...')
        r = c.send(n)
        print('return %s'%r)
    c.close()

c = comsume()
product(c)