# Ordinary vs Anonymous functions
#     We don't define the anonymous functions using the 'def' keyword 
#     We instead define the function using a lambda expression and save it in a variable
#     Usually a very short function ; A one-liner of code

mysquare = lambda x: x*x
# mysquare is now a callable function
print(mysquare(4))

mysum = lambda x,y: x+y
print(mysum(3,5))

mysum2 = lambda *args: sum(args) # '*args' is equal to 'x,y,z,...' as many arguments 

lst = [1,2,3,4]
p1, *p2, p4 = lst
print(p2)
print(mysum2(*lst))

print((lambda x: x**3)(5))


# You use Anonymous and lambda functions when you need to pass functions into other functions but the functions passed in are not complicated
numbers = [8,66,12,14,15,7,8,99]

def filter_func(x):
    return x%2==0
print(list(filter(filter_func, numbers)))

print(list(filter(lambda x: x%2==0, numbers))) # iterators are more memory efficient than lists

print(list(map(lambda x: x*x, numbers)))


# You can pass in a value and get a function
# Return a function
def myfunc(num):
    return lambda x: x*num
ten_mult = myfunc(10)
print(ten_mult(20))