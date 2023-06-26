import threading 
import time

def func():
    print('ran')
    time.sleep(2) # While this thread is sleeping the CPU will switch to the main thread
    print('done')

x = threading.Thread(target=func) # Threads are assigned to a function
x.start() # Thread only starts when this is called
print(f'Number of active threads: {threading.active_count()}') 