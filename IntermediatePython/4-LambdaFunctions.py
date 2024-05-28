#     small one line anonymous function that is defined without a name
add10 = lambda x: x + 10 #<function <lambda> at 0x000002783C9FC400>
n = add10(5) #15
def add10_func(x): #both lambda and this function do the same thing
    return x+10
mult = lambda x,y: x*y #<function <lambda> at 0x000001C20F5FC220>
n = mult(2,7) #14
#lambda functions are used when you need a simple function that is used only once or as an argument to higher order function (functions that take other functions as arguments)
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D) #[(1,2), (5,-1), (10,4), (15,1)]; sorts the list in terms of the first item per tuple
points2D_sorted = sorted(points2D, key=lambda x: x[1]) #[(5,-1), (15,1), (1,2), (10,4)]; each x is a tuple in the list; key is a function
points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1]) #[(1,2), (5,-1), (10,4), (15,1)]
# (map(func, seq))
a = [1,2,3,4,5]
b = map(lambda x: x*2, a) #<map object at 0x000001BE81597160>
b = list(b) #[2,4,6,8,10]
c = [x*2 for x in a] #[2,4,6,8,10]; list comprehension
# (filter(func, seq)); func returns true or false; returns all objects for which the function evaluates to true
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0,a) #<filter object at 0x000001E075886EF0>
b = list(b) #[2,4,6]
c = [x for x in a if x%2==0] #[2,4,6]
# (reduce(func, seq))
from functools import reduce
a = [1,2,3,4]
reduce_a = reduce(lambda x,y: 3*x+y,a) #58; repeatedly applies the function to the elements and returns a single value; the accumulated value is (x) while the last transversed item is y
