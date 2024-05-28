from multiprocessing import Process, Lock, Queue, Array

def square(numbers,queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)


if __name__ == '__main__':
    q = Queue()

    numbers = range(1,6) #no need to make into shared_array, since we're not processing it directly

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers,q))
                 
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    while not q.empty():
        print(q.get()) #both processes can access the queue
    