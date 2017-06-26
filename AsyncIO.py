import asyncio

# @asyncio.coroutine
# def hello():
#     print('start coruntine')
#     r = yield from asyncio.sleep(1)
#     print('end coruntine')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

import threading

# @asyncio.coroutine
# def hello():
#     print('start, %s '%threading.current_thread())
#     r = yield from asyncio.sleep(1)
#     print('end,%s'%threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

async def hello():
    print('start %s'%threading.current_thread())
    r = await asyncio.sleep(1)
    print('end %s'%threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



# @asyncio.coroutine
# def wget(host):
#     print('connect to %s'%host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n'%host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.baidu.com','www.sohu.com','www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()