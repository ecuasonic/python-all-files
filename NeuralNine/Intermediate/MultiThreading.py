# Allows for speeding up code by executing multiple tasks at the same time
# MultiThreading is considered lightweight-processes ; they need less resources
# Threads share memory space ; BIG advantage for multithreading
# We can execute two functions at the same time, working in parallel

import threading

def function1():
    for x in range(10):
        print("ONE")

def function2():
    for x in range(10):
        print("TWO")

t1 = threading.Thread(target=function1) # referring to function without calling it
t2 = threading.Thread(target=function2)

t1.start()
t2.start()

t1.join()
t2.join()




def hello():
    for x in range(50):
        print("Hello")

t3 = threading.Thread(target=hello)
t3.start()

t3.join() # Holds the main thread in place until t3 is done 
print("Another Text")




import time

x = 8192

lock1 = threading.Lock()

def double():
    global x,lock1
    with lock1:
        while x < 16384:
            x *= 2
            print(x)
        print("Reached the maximum!")

def halve():
    global x,lock1
    with lock1: # using the same lock as in double(), and as soon as the thread comes out of lock, it skips in line to run again 
        # double() has no time to look if the lock is available, halve() doesn't even know that there is a lock so it runs through the lock again unhindered
        while x > 1:
            x /= 2
            print(x)
        print("Reached the minimum!")

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

t1.join()
t2.join()




semaphore1 = threading.BoundedSemaphore(value=5) # a lock is like a semaphore with value=1

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    with semaphore1:
        print(f"{thread_number} was granted access!")
        time.sleep(.1)
        print(f"{thread_number} is now releasing")

threads = []

for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    threads.append(t)
    t.start()
    time.sleep(.01)

for t in threads:
    t.join()




event1 = threading.Event()

def myfunction():
    print("Waiting for event to trigger...\n")
    event1.wait() # branch thread stops here until event is triggered
    print("Performing action XYZ now...")

t1 = threading.Thread(target=myfunction)
t1.start()

#x = input("Do you want to trigger the event? (y/n)\n") # main thread waits here for input
x = 'y'
if x == 'y':
    event1.set() # triggers the event




path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read() #sets text to the contexts of the text file ; restarts every 3 sec
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text) # prints the text every 1 sec with 3 sec update, 30 times
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True) # thread is terminated when main thread is terminated
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

t1.join()
t2.join()