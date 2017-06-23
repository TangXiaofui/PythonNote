import os
# print('process %s start'%(os.getpid()))
# print('------------------------------------')
# unix/linux/mac
# pid = os.fork()
# if pid == 0:
#     print('this is child process %s , father process %s '%(os.getpid(),os.getppid()))
# else:
#     print('this is father process %s,parent %s'%(os.getpid(),os.getppid()))


def printProcess(name):
    print('run process %s %s,parent id %s '%(name,os.getpid(),os.getppid()))


from multiprocessing import Process, Pool,Queue
import time, random
def long_time_task(name):
    printProcess(name)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %s'%(name,(end-start)))

def write(q):
    printProcess('write')
    for x in ['a','b','c']:
        q.put(x)
    time.sleep(random.random()*3)

def read(q):
    printProcess('read')
    while True:
        value = q.get(True)
        print('get %s',value)

if __name__ == '__main__':
    # printProcess('main')
    # p = Process(target=printProcess,args=('child',))
    # print('Child will start')
    # p.start()
    # p.join()
    # print('child process end')


    # p = Pool()
    # for i in range(17):
    #     p.apply_async(long_time_task,args=(i,))
    # print('waiting ')
    # p.close()
    # p.join()
    # print('All process done')

    # import subprocess
    #
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)

    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

