def mydecorator(func):
    
    def wrapper(*args, **kwargs):
        print("I am decoratoring your function!")
        result = func(*args, **kwargs)
        return result
    
    return wrapper

@mydecorator
def hello_world(name):
    print(f"Hello World and {name}")

hello_world("Richard")

# Practical Example #1 - Logging

def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = func.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10,20))

# Practical Example #2 - Timing
import time
from typing import Any

def dec_timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper

@dec_timed
def myfunc(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

myfunc(10000)

# Class Decorators
class myDecorator():
    def __init__(self, func):
        self.func = func
        self.amount = 0

    def __call__(self, *args, **kwargs):
        self.amount += 1
        print(f'This method has executed {self.amount} times')
        return self.func(*args, *kwargs)
    
@myDecorator # creates instance of myDecorator class, with HelloWorld as func input ; HelloWorld is now a myDecorator object
# HelloWorld = myDecorator(HelloWorld)
def HelloWorld(name):
    print(f'Hello {name}')

HelloWorld("Rich") # calls on myDecorator object 




