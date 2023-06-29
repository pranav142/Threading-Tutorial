import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process, cpu_count

"""
What is the difference between multiprocessing and multithreading

1. In multi threading threads are run concurently meaning that threads arent running simultaneously but rather when other threads/tasks arent working another thread can be activated, threads will usually share same memory space and interpreter instance

2. In multi processing there are multiple processes each with its own python interpreter instance and memory space, in multi processing tasks can be distributed over variety of cores on a CPU this means processes can run simultaneously rather than concurrently
"""
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

    # CODE SNIPPET 2: This code snippet uses threading so when io_boudn is sleeping the next thread can continute to execute
    
    # for _ in range(2):
    #     x = Thread(target=io_bound, args=(SLEEP,))
    #     x.start()
    
    # x.join()
    
    # CODE SNIPPET 3: CPU bound task used for counting, goes sequentially Finished
    # in approx 16 seconds

    # cpu_bound(COUNT)
    # cpu_bound(COUNT)

    # CODE SNIPPET 4: CPU Bound tasks with threading, this also took 16 seconds
    # global interpreter lock 

    # t1 = Thread(target = cpu_bound, args =(COUNT, ))
    # t2 = Thread(target = cpu_bound, args =(COUNT, ))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    
    # CODE SNIPPET 4: CPU Bound tasks with multi processing, this finished in 8 seconds
    # nearly half the time of the previous segments. 

    # processes = []
    # print(f'number of logical processors {cpu_count()}')
    # for i in range(cpu_count()):
    #     p = Process(target=cpu_bound, args=(COUNT,))
    #     p.start()
    #     processes.append(p)

    # for p in processes:
    #     p.join()

    # Code Snippet 5: Multi process for io_bound tasks
    p1 = Process(target = io_bound, args =(SLEEP, ))
    p2 = Process(target = io_bound, args =(SLEEP, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)