"""
Semaphores
    1. Control which threads can acess a resource
    2. When a thread accesses a resource the semaphore value is decremented, 
    when the semaphore value is 0 no other thread can access that resource until the 
    semaphore has a non-0 value.
    3. Types
        a. Mutex -- semaphore only has values 1 and 0 which means only one thread can access
        a resource at a time 
        b. counting semaphore -- semaphore can take on multiple non-negative values which means
        more that one thread can acess a resource at a time but the amount is limited
        by the largest value the semaphore has
"""

import threading
import time
# global variable x
x = 0
  
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
  
def thread_task(lock): # We pass in the lock so if another thread tries to acquire a lock that already has a lock acquired then that thread will not execute the resource
    """
    task for thread
    calls increment function 100000 times.
    """
    
    for _ in range(100000):
        lock.acquire() # when a thread performs this task it acquires a lock which prevents any other thread from accessing this resource
        increment()
        lock.release() # only once the lock is released can another thread access this resource
  
def main_task():
    global x
    # setting global variable x as 0
    x = 0
  
    # creating a lock
    lock = threading.Lock() 
  
    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
  
    # start threads
    t1.start()
    t2.start()
  
    # wait until threads finish their job
    t1.join()
    t2.join()
  
if __name__ == "__main__":
    for i in range(10):
        main_task()
        print(f"Iteration {i}: x = {x}")