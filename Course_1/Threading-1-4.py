import concurrent.futures
import time

# Thread Pools: Collection of threads that can be reused for multiple tasks

def worker():
    print('starting work')
    time.sleep(2)
    print('Done')

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2) # Maximum number of threads in this pool is 2

for _ in range(3): 
    pool.submit(worker) # Because we are creating three instances but the max number of threads in this pool is two the worker function will be exectued a max of two times concurrently until one of the threrads completes its execution then that thread will be used to perform the task a third time

pool.shutdown() # similar to .join() this ensures all of the threads have completed their execution before the program continues

print('Main Thread Activated')