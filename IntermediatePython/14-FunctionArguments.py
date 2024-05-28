"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""



# Parameters are the variables that are defined or used inside parentheses when defining a function
# Arguments are the values passed for these parameters while calling a function
def print_name(name): # 'name' is the parameter
    print(name)
print_name('Alex') # 'Alex' is the argument



def foo1(a,b,c,d=4): # the default value for d is 4
    #default parameters must be at the end
    print(a,b,c,'default value:',d, ', keywords have to be at end and can be out of order')

foo1(1,2,3) # positional arguments
foo1(b=2,c=3,a=1) # keyword arguments
foo1(1, c=3,b=2) #mix of both positional and keyword arguments
# keyword arguments have to be at the end, just like with default parameters



def foo2(a,b, *args, **kwargs): # args are tuples and kwargs are dictionaries
    #it doesn't matter if we use *a or **k, if there is asterisk(s) then it will be defined as a variable-length argument
    print('positional arguments:',a,b)
    for arg in args:
        print(arg, 'in args')
    for key in kwargs:
        print(key, kwargs[key], 'in kwargs')

foo2(1,2,3,4,5, six = 6, seven = 7)



# Force keyworld arguments 
#   have to include c,d arguments as keyword arg in foo3
def foo3(a,b, *, c, d): 
    print(a,b,c,d, 'asterisk was used as parameter to force inclusion of following parameters as kwargs')

foo3(1,2,c=3,d=4)



# Force to include keyword arguments after any postional argument
#   have to include c,d arguments as keyword arg in foo3
def foo4(*args, c, d): 
    for arg in args:
        print(arg)
    print(c,d, 'used *args as parameter ; force inclusion of following parameters as kwargs')

foo4(1,2,c=3, d=4)



def foo5(a,b,c):
    print(a,b,c, 'list/tuple/dict unpacking as postional arguments with (*)')
    #the list/tuple has to be the same length as there are parameters

my_list = [0,1,2]
foo5(*my_list) #unpacking list into foo5 arguments

my_tuple = (0,1,2)
foo5(*my_tuple) #unpacking tuple into foo5 arguments

my_dict = {'c':3, 'b':2, 'a':1}
foo5(*my_dict) #unpacks dict keys in order
foo5(**my_dict) #unpacks dict values, but keys have to be equal to parameters (positional)



def foo6():
    x = number #global variable
    #number = 3 ; this will render 'number' as a local variable that is different from the global variable
    print('Accessing globle variable:',x)
number = 0
foo6() # the number is accessable through the function as is

def foo7():
    global number # this part allows the function to access and modify the number
    # without this line, 'number' is created as a local variable within the function
    x = number
    number += 1
    print('Modifying global variable:',x)
    print(f"Old 'Number': {x}, New 'Number': {number}")
foo7()



# Parameter Passing
#     'Call by value' or 'Call by reference'
#     'Call by object' or 'Call by object reference'
#     Parameters passed in are references to an object, but the reference are passed by value

# Mutable objects, like lists or dictionaries, can be changed within a method
#     but if you rebind the reference in the method, then the original reference (created outside the function) will still point to the original object
#     and is not changed

# Immutable objects, like integers or strings cannot be changed within a method
#     But immutable objects contained within a mutable object can be reassigned within a method

def foo8(x):
    x = 5
var = 10
foo8(var) # there is no change to 'var'
# 'var' is an integer, which is an immutable object and cannot be changed
#      A local variable x is created within the function

def foo9(a_list):
    a_list.append(4)
    a_list[0] = -10
my_list = [1,2,3]
foo9(my_list) # appends 4 to the list and changes the first element to -10
# Mutable objects can be mutable within a function
#     Even if the list elements are immutable objects, such as integers/tuples/strings

def foo10(a_list):
    a_list = [100,200,300]
    a_list = a_list[:1]
    a_list = a_list + [100,200,300] # USE "a_list += [100,200,300]" INSTEAD

    a_list.append(4)
    a_list[0] = -10
my_list = [1,2,3]
foo10(my_list) # there is no change to 'my_list'
# A local variable is created when a_list reference is rebinded
# If the a_list is attempted to be reassigned to another list, then the function will create a local variable with the same name

def foo11(a_list):
    temp = a_list
    temp = temp[:1]

    a_list.append(4)
    a_list[0] = -10
    temp.append(4)
    return temp
my_list = [1,2,3]
new_list = foo11(my_list) #new_list is a splice version of my_list, which wasn't possible in foo10()
# my_list is modified in this code





