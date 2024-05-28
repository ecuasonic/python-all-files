
#function and class decorators
#    function decorators are more common

#a decorator is a function that takes in another function as argument and extends the behavior of the function without explicitly modifying it
#    in other words, it allows you to add new functionality to an existing function 

#functions in Python are first-class objects
#    this means that like any other object, they can be defined inside another function passed as an argument to another function
#    and even returned from other functions

#The purpose of "return wrapper" is to return the wrapper function itself, which will be used as a replacement for the original function
#    The decorator effectively reassigns the function name to the wrapper function
#    So when calling the decorated function, the wrapper function is invokes, which then calls the original function 

import functools #helps to maintain identity of the original function 

def start_end_decorator(func):

    @functools.wraps(func) #this will preserve the information of the original function
    def wrapper(*args, **kwargs): #use as many arguments and keyword arguments ; arguments used after reassingment 

        print('Start')
        result = func(*args, *kwargs) # func is assigned to the original function, so when the og function is assigned to wrapper, the functionality is not lost and no assignment loop is created
        print('end')
        return result
    
    return wrapper #this ensures that the wrapper function is returned and can be used as a replacement for the original function

#'print_name = start_end_decorator(print_name)' ; the print_name function is assigned to the returned wrapper function

@start_end_decorator #the addition of this part assigns the function print_name to wrapper, similar to 'print_name = start_end_decorator(print_name)'
#this adds more to the function itself
#the decorator will apply itself to the next runnable line of code
def print_name():
    print("Alex")

print_name()

@start_end_decorator
def add5(x):
    return x+5 #****************when returned, the output needs to be assigned to something upon being returned************

print(help(add5))
print('')
print(add5.__name__) #prints out the function name

def my_decorator(func):

    @functools.warps(func)
    def wrapper(*args, **kwargs):
        # Do..
        result = func()
        # Do..
        return result
    return wrapper


def repeat(num_times): #needed to input values into decorator; the value is stored for later use 
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs): #greet = wrapper; 'name' falls under *args
            for _ in range(num_times):
                result = func(*args, **kwargs) #performs print but returns None each time
            return result #'print' returns None
        return wrapper
    return decorator_repeat


@repeat(num_times=4) # @repeat(4) also works 
#repeat(num_time=4) returns decorator_repeat, which then replaces repeat(num_times = 4) as the new decorator
#greet = repeat(num_times)(greet) ; repeat(num_times) returns the decorator function, which then runs with 'greet' as input
def greet(name):
    print(f'Hello {name}')
    
greet('Alex')
k = 10000000
from timeit import default_timer as timer
start = timer()
lst = [0]*k
stop = timer()
print(stop-start)

start = timer()
lst = range(k) #range(k) is faster than [0]*k
stop = timer()
print(stop-start)

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args] #repr(a) converts the args into their string representations ["'Alex'"]
        kwargs_repr = [f'{k} = {v!r}' for k, v in kwargs.items()] # '!r' makes sure that the {} input is represented as it is
        #if string, then it will look like a string within a string ; 'this means that 'hello' would look like this'
        signature = ", ".join(args_repr + kwargs_repr) # "'Alex', 'Another'"
        print(f'Calling {func.__name__}({signature})') # when including string into f-string, the outer quotes are removed 
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper

@debug #debug is run first
@start_end_decorator #start_end_decorator is run second
def say_hello(name, temp):
    greeting = f'hello {name} and {temp}'
    print(greeting)
    return(greeting)

say_hello('Alex', 'Another')

#A class decorator do the same thing as function decorators
#    but they are typically used if we want to maintain and update a state across all instances of a function.
class CountCalls:


    def __init__(self, func): #an input has to include a function, since __call__ invokes func
        self.func = func # func is stored as an instance variable
        self.num_calls = 0

    def __call__(self, *args, **kwargs): #this allows instances of the class to be callable, just like functions
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
#say_hello = CountCalls(say_hello)
def say_hello():
    print('Hello')

say_hello() # now calls say_hello.__call__()

#you can use timer, debug, check arguments, plug-in, cache, update info/state with decorators
