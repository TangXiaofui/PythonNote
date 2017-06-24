import time,threading

def loop():
    n = 0
    while n < 5:
        n = n + 1
        print('current thread name %s ,num = %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('current thread %s '%(threading.current_thread().name))



# t = threading.Thread(target=loop,name='test')
# t.start()
# t.join()


balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


local_school = threading.local()

def print_student():
    std = local_school.name
    print("hello,%s (thread in %s )" %(std,threading.current_thread().name))

def process_run(name):
    local_school.name = name
    print_student()

t3 = threading.Thread(target=process_run,args=('txh',),name='thread A')
t4 = threading.Thread(target=process_run,args=('ttt',),name='Thread B')
t3.start()
t4.start()
t3.join()
t4.join()
