#generators are functions that return an object that can be iterated over
#    just like regular functions, but use "yield" instead of "return"

def mygenerator(): #generator function 
    yield 1 # each 'yield' statement pauses the execution of the generator and returns a value to the caller
    yield 2
    yield 3

g = mygenerator() # iterable 
# Doesn't execute the function immmediately. 
#     Instead, it returns a generator object without executing any code inside the function

value = next(g) #executes the code inside 'mygenerator' until it encounters a 'yield statement'
# The value following the 'yield' keyword is returned, and the state of the generator object is saved
print(value)

value = next(g) # resumes from the point where it was paused, and until the next 'yield' statement is encountered
print(value)

value = next(g)
print(value)

try:
    value = next(g)
    print(value)
except StopIteration:
    print("No more values to yield from the generator") #the StopIteration has no message to print



g = mygenerator()
print(sum(g)) #6 ; can be used in functions that have iterables as arguments

g = mygenerator()
print(sorted(g)) # [1,2,3]



def countdown(num):
    print('Starting')
    while num > 0:
        yield num #when iterated, it stops here and outputs num. When called again, it does num -= 1 and continues in the loop
        num -= 1

cd = countdown(4)
for i in cd:
    print(i)


import sys
k = 1
def firstn(n): #return a sequence 0 to n-1 in the form of a list
    nums = list()
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

lst = firstn(k)
print(sys.getsizeof(lst)) #920 bytes ; stores list in term of binary 
#print(sum(lst))


def firstn_generator(n): #returns a sequence 0 to n-1 in the form of a generator object
    num = 0
    while num<n:
        yield num
        num +=1

g = firstn_generator(k)
print(sys.getsizeof(g)) #200 bytes ; always 200 bytes, regardless of size
#print(g)
#print(sum(g))
print(sys.getsizeof(g)) #200 bytes



def fibind(n):
    a,b = 0,1
    while n >= 0:
        yield a
        a,b = b, a+b
        n -= 1

def fiblim(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

#generator expressions are written like list comprehension, but with () instead of []
#    shortcut to implement generator objects

mygenerator = (i for i in range(10) if i%2 == 0) #creates generator object

lst = list(mygenerator)
print(lst)
