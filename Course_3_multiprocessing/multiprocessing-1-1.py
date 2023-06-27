import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

"""
What is the difference between multiprocessing and multithreading

1. In multi threading threads are run concurently meaning that threads arent running simultaneously but rather when other threads/tasks arent working another thread can be activated, threads will usually share same memory space and interpreter instance

2. In multi processing there are multiple processes each with its own python interpreter instance and memory space, in multi processing tasks can be distributed over variety of cores on a CPU this means processes can run simultaneously rather than concurrently
"""

import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process
 
 
COUNT = 200000000
SLEEP = 10
 
def io_bound(sec):
 
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished sleeping...")
 
def cpu_bound(n):
 
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start counting...")
 
    while n>0:
        n -= 1
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...")
 
if __name__=="__main__":
    start = time.time()
 
    # CODE SNIPPET 1: This code is runing the io_bound task all on the main thread
    # This means the second io_bound() can only occur once the first has finished
    # This leads to 20 second completion time

    # io_bound(SLEEP) 
    # io_bound(SLEEP)

    # CODE SNIPPET 2
    
    for _ in range(2):
        x = Thread(target=io_bound, args=(SLEEP,))
        x.start()
    
    x.join()
    
    end = time.time()
    print('Time taken in seconds -', end - start)