import time,threading

def loop():
    n = 0
    while n < 5:
        n = n + 1
        print('current thread name %s ,num = %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('current thread %s '%(threading.current_thread().name))



t = threading.Thread(target=loop,name='test')
t.start()
t.join()