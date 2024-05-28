'''
Process: An instance of a program (e.g. a Python interpreter)

+ Takes advantage of multiple CPUs and cores -> parallel processes have a seperate memory space
+ Seperates memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is stated independently from other processes
+ Processes are interruptable/killable
+ One GIL (Global Interpreter Lock) for each process -> avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication) is more complicated
- Since processes have seperate memory spaces, memory sharing is complicated
'''

'''
Threads: An entity within a process that can be scheduled (also known as "lightweight process")
A process can spawn multiple Threads

+ All threads within a process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for I/O-bound tasks (Input-Output tasks)
    * When program has to talk to slow devices, like a hard drive or a network conncetions, then with threading, 
      your program can use the time waiting for these devices and then intelligently switch to other threads and do the processing in the meantime

- Threading is limited by GIL: Only one thread at a time
    * No parallel computation in multithreading
- No effect for CPU-bound tasks
- Not interruptable/killable
    * Be careful with memory leak here
- Careful with race conditions
    * Occurs when two or more threads want to modify the same variable at the same time 
'''

'''
GIL: Global interpreter Lock
- A lock that allows only one thread at a time to execute in Python

- Needed in CPython because memory management is not thread-safe
    * CPython is the reference Python implementation that you get when you download and install Python from python.org
    * In CPython, there is a technique called 'reference counting' for memory management
        * This means that objects created in Python have a reference count variable that keeps track of the number of reference that point to the object
        * When this count reaches zero, the memory occupied by the object can be released

        *The problem now in multi-threading is that this reference count variable needs protection from race conditions 
         where two threads increase or decrease the value simultaneously 

        *If this happens, it can either cause leaked memory that is never released
         or it can incorrectly release the memory while a reference to that object still exists

- To avoid GIL:
    - Use multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
'''

#with threading and multiprocessing, code can be run in parallel and speed up code

from multiprocessing import Process
import os 
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

# The "if __name__ == '__main__':" guard statement prevents the spawned processes from execute the code inside the block 
#     Process recursion (infinite loop of creation)
#     Duplicated execution (main module and processes run same code)
#     Module import issues (any executable code outside the guard will be executed)
#     Unneccesary resource consumption: Code imported even though not needed

if __name__ == '__main__': 
    processes = []
    num_processes = os.cpu_count() #16

    # The main module is responsible for creating and managing the processes
    # When the main module creates processes using the 'multiprocessing' module,
    #     each process imports the necessary modules and functions from the main module
    # Functions are effectively imported and available in each spawned process
    #     The processes inherit the functions

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers) #target is either a callable object or a function, args=() would be used if arguments were needed
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join() # While waiting for all the processes to finish, the main thread is blocked

    print('processes done') #only reach this point when all processes are done

from threading import Thread
import os 
import time

threads = []
num_threads = 10

if __name__ == '__main__':

    #create thread
    for _ in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    #start threads
    for t in threads:
        t.start()

    #join threads
    for t in threads:
        t.join()

    print('threads done')


