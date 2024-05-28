from threading import Thread, Lock, current_thread
from queue import Queue
import time

# A queue is a linear data structure the follows the FIFO (First-In-First-Out principle)
#     Customers waiting in single-filed line
#     Not iterable

if __name__ == '__main__':

    q = Queue() #

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 -->
    first = q.get() #gets the first in queue
    q.task_done() 
    # Tracks Completed Tasks: 
    #    Informs the queue that a task as been processed and is now considered completed
    #    The queue keeps track of the number of complete tasks internally
    # Synchronization with 'join()':
    #     Plays a crucual role in synchronization when used together with the 'join()' method of the queue.
    #     The 'join()' method blocks the calling thread until all tasks in the queue have been processed and marked as completed with 'task_done()'
    #     It allows you to wait until all tasks have been handled before proceeding with futher code execution

    # You should always ensure that each task retrieved from the queue corresponds to a call to 'task_done()'
    #     Failure to do so can result in issues like deadlocks or incorrect synchronization
    #     

    q.get()
    q.task_done()

    q.get()
    q.task_done()

    print(q.empty())
    q.join() # blocks until all items in the queue have been gotten and processed 
    # similar to the thread.join() method


    print('end main')



# With a queue, data can be easily exchanged in a thread-safe environment

def worker(q,lock):
    while True:
        #value = q.get() #if there is no values in the queue, then the q.get() will block and wait until items are available
        #thread-safe

        #processing
        # At this point, all threads arrive in order
        # As the threads process, they can start to get clutted up, especially when heading to the back of the line
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}') #threads might try to print at the same time
        q.task_done() #it takes time to even observe these functions
                            #include this outside to prevent the same thread from 'cutting in line'
        time.sleep(0.1) #the time portion is entirely negligable, the time to observed the function is enough to allow other threads to hop in 


if __name__ == '__main__':
    lock = Lock()
    q = Queue()

    num_threads = 10
    for i in range(1,21):
        q.put(i) #thread-safe
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True # If the main program completes before all the worker threads finish their execution, the program will exit immediately
                                    #regardless of whether the worker threads have finished processing all the tasks 
                                    #the worker() function includes an infinite loop, which is why we need this
        thread.start() # all the threads wait at the value = q.get() line in worker(q), until value is put into queue

    '''for i in range(1,21):
        q.put(i) #thread-safe'''

    q.join()

    print('end main')