from multiprocessing import Process, Value, Array, Lock
import time

def add_100F(number,lock): #race conditions are an issue in multiprocessing as well
    for i in range(100):
        time.sleep(0.001)

        with lock: # Locks also work in multiprocessing
            number.value += 1

def add_100A(numbers,lock): 
    for i in range(100):
        time.sleep(0.001)
        with lock:
            numbers[:] = [num+1 for num in numbers[:]] 
            #the [:] ensures the the value is shared across processes
            # If [:] is not included, then numbers is created and saved locally

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    # first input is the data type ; 'i' for integer, 'd' for double
    # second input is the starting value
    print('Number at beginning is', shared_number.value)
    print('Array at beginning is', shared_array[:])

    p1 = Process(target=add_100F, args=(shared_number,lock))
    p2 = Process(target=add_100F, args=(shared_number,lock))
    p3 = Process(target=add_100A, args=(shared_array,lock))
    p4 = Process(target=add_100A, args=(shared_array,lock))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print('Number at end is', shared_number.value)
    print('Number at beginning is', shared_array[:])
