print(complex(10,1)) # complex function
print(10//3) # floor function
x = 2
if type(x) is int:
    print(f'{x} is of type {type(x)}')

try:
    print("Outer try block")
    try:
        print("Inner try block")
        # Code that may raise an exception
        raise ValueError("Exception in inner try block")
        print('After')
    finally:
        print("Inner finally block") # finally mostly used for nested try/finally blocks, and for try-except-finally code organization
except ValueError as e:
    print("Caught exception:", e)
finally:
    print("Outer finally block")

x = 100
y = 1

assert x > y, "x should be larger than y" # raises an assertion error otherwise

file = open('file.txt', 'w') # creates file is not exists ; 'r' will raise exception 
file.write("Hello")
file.flush() # Similar to conn.commit() in sqlite3 API
file.close() # Similar to conn.close()

file = open('file.txt', 'a')
file.write(" Hello again")
file.flush()
file.close()

from os import * # import the entire module, then use function/classes directly

#Strings
#    \t tab
#    \b backspace
#    \s spac

text = "This is my text!"
text = text.title() #Uppercases first letter of each word
text = text.swapcase() #Swaps cases
num = text.count('is')
ind = text.find('is')
text = text.replace('is', 'was')