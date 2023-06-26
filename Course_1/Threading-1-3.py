import threading
import time

ls = []

def add_to_list(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

for _ in range(2):
    x = threading.Thread(target=add_to_list, args=(5, ))
    x.start()

x.join() # This stops the main thread from executing the print statement until the threads have finished executing

print(ls) # This code will prematurely stop once both add_to_list (x) threads are sleeping, this is because both threads are modifying a vriable and once this print statement occurs then the program will stop, to prevent premature printing we use .join()