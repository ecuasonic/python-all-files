'''
a = 5 print(a')) ; SyntaxError: invalid syntax
a = 5 + '10' ; TypeError: unsupported operand type(s) for +: 'int' and 'str'
import somemodule ; ModuleNotFoundError: No module named 'somemodule'
a = c ; NameError: name 'c' is not defined
f = open('somefile.txt') ; FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'
a = [1,2,3]
a.remove(4) ; ValueError: list.remove(x): x not in list
a.index(4) ; IndexError: list index out of range
d = {'name':'Max}
d['age] ; KeyError: 'age'
x = -5
if x<0:
    raise Exception('x should be positive') ; Exception: x should be positive
assert (x>=0) ; Assertion Error
assert(x>=0), 'x is not positive' ; AssertionError: x is not positive
a = 5 / 0 ; ZeroDivisionError: division by zero'''
try:
    a = 5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e) #division by zero
except TypeError as e:
    print(e)
else:
    print('everything is fine')
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e) #unsupported operand type(s) for +: 'float' and 'str'
else:
    print('everything is fine')
try:
    a = 5/1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: #runs if no exception
    print('everything is fine') #everything is fine
finally: #always runs, no matter if there was an exception; used to make clean up operations 
    print('cleaning') #cleaning
class ValueTooHighError(Exception): #This class is inherited from the built-in 'Exception' class
    #this is why you can add a message to the exception, without an __init__ in this class
    pass
#raise ValueTooHighError('value is way too high') #ValueTooHighError: value is way too high
print(ValueTooHighError('value is way too high')) #value is way too high
class ValueTooSmallError(Exception): #defines custom exception class that can be used to raise exceptions with a specific error message and associated value
    def __init__(self, message, value): #__init__ method is the constructor for the class
        #__init__ method is a special method that is called when an object is instantiated from the class
        #primary purpose is to initialize the attributes of the object
        #the parameters of the __init__ method are what is inputed into the overall class
        #the self.message and self.value are the attributes that every member of the class have
        #both message and value are arbitrary and can be exchanged for one another
        #you can add more than just message and value (as many inputs)
        self.message = message #used to store message when exception occurs
        self.value = value #used to store the value that caused the exception
    pass
def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high') #raises the exception; skips into the corresponding except's
    if x<5:
        raise ValueTooSmallError('value is too small',x) 
try:
    test_value(1)
except ValueTooHighError as e:
    print(e) #value is too high
except ValueTooSmallError as e:
    print(e.message, e.value) #value is too small 1
e = ValueTooSmallError('value is too small', 3) #ValueTooSmallError: ('value is too small', 3) ; in other classes, this shows up as memory location
e.message #'value is too small'
e.value #3
