import threading
import time
import os

def count(n):
    print(f'Current Thread: {threading.current_thread().name}')
    print(f"ID of process running task: {os.getpid()}") # Process ID will be the same
    for i in range(1, n+1):
        print(i)
        time.sleep(0.1) # when this thread goes to sleep the cpu will switch to next thread that still is targeted with this function

for _ in range(2):
    x = threading.Thread(target=count, args=(10,))
    x.start()
    # x.join() # .join() here would mean anytime a thread is initialized another one wont be able to be initialized and the main thread cant start until this thread finishes execution

print(f"ID of process running main program: {os.getpid()}")

# print name of main thread
print(f"Main thread name: {threading.current_thread().name}")

x.join() # .join() essentiially says to not continue this program until the thread x has finished its execution, 

print('done') # When both count threads are sleeping the cpu will switch back to the main thread causing this line to be executed prematurely this is why we use .join()