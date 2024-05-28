# The technique of a function calling itself
# Potential of endless loop, called StackOverFlow Error

# Non-Recursively
n = 7
fact = 1
while n > 0:
    fact = fact*n
    n -= 1
print(fact)

# Recursively
def factorial(n):
    out = n
    if n < 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(7))

# Sometimes the iterative function is faster than the recursive function 

def fib(n):
    a,b = 0,1
    for x in range(n):
        a,b = b, a+b
    return a
    # each one spawns one more (linear growth)
    # approximatley n calculations, with all being distinct (no repeating calculations)
    # MUCH more efficient


print(fib(40))

def fibR(n):
    if n <= 1: return n
    else:
        return fibR(n-1)+fibR(n-2) 
        # each one spawns two more (exponential growth), with makes it much slower in comparision with iterative function
        # approximately 2^n calculations, and some of the calculations are repeatedly done multiple times 
        # very inefficient

print(fibR(40))