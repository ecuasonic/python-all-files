from threading import Thread, Lock
import time

database_value = 0

def increase1(): #race condition
    global database_value

    local_copy = database_value

    #processing
    local_copy +=1
    time.sleep(0.1)
    #thread1 stops here for 0.1 seconds, thread2 is started, but the database_value is still zero

    database_value = local_copy
    #thread1 copies over to database_value (1) and thread2 copies the same thing (1)
    #example of race conditions, when both threads are modifying variables at the same time



def increase2(lock): #lock prevents race conditions
    global database_value

    lock.acquire() # this prevents another thread to access this code at the same time
    local_copy = database_value

    #processing
    local_copy +=1
    time.sleep(0.1)

    database_value = local_copy

    lock.release() # allows the next thread in queue to access the code after lock.acquire()



def increase3(lock): #using lock as context manager
    global database_value

    with lock: 
        local_copy = database_value

        #processing
        local_copy +=1
        time.sleep(0.1)

        database_value = local_copy


if __name__ == '__main__':

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase3, args=(lock,))
    thread2 = Thread(target=increase3, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')