# coding=utf-8
import threading
mydata = threading.local()
mydata.number = 42
print(mydata.number)
log = []


def f(n):
    mydata.number = n
    log.append(mydata.number)
    log.append('---')


print('这是主线程：', threading.current_thread().name)
thread = threading.Thread(target=f, args=(5, ))
thread2 = threading.Thread(target=f, args=(6, ))
print(thread.name, thread2.name)
thread.start()
thread2.start()
thread2.join()
thread.join()
print(log)
print(mydata.number)
