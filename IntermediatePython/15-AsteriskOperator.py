# The askerisk (*) is used for:
#      muliplication/power operations,
#      the creation of lists/tuples with repeated elements, 
#      for args/kwargs and keyword-only parameters,
#      for unpacking lists/tuples/dictionaries into function arguments,
#      for unpacking containers,
#      and for merging containers into a list or merging two dictionaries

print(f'The product of 5 and 7 is {5*7}')
print(f'The power of 2 to 4 is {2**4}')

print(f"List with 10 repeated (a,b) values: {['a','b']*10}")
print(f"Tuple with 10 repeated (a,b) values: {('a','b')*10}")
print(f"String with 10 repeated (a,b) values: {'ab '*10}")

def foo1(a,b,c,*args,**kwargs):
    print(a,b,c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
    print('done foo1\n')
foo1(1,2,3,4,key1='hello', key2=100)

def foo2(a,b,*,c):
    print(a,b,c, 'kwargs enforce')
    print('done foo2\n')
foo2(1,2,c=3)

my_list = [1,2,3]
foo1(*my_list)

my_tuple = (1,2,3)
foo1(*my_tuple)

my_dict = {'a':1, 'b':2, 'c':3}
foo1(*my_dict)
foo1(**my_dict)

numbers = range(10)
*beginning, last = numbers #creates tuple with last being numbers[-1], and beginning the first section of numbers (always unpacks to a list)
print(beginning, last)

tuple = (1,2,3,4,5)
*beginning, last = tuple
print(beginning, last)

dict = {'a':1, 'b':2, 'c':3}
*beginning, last = dict
print(beginning, last)

set = {1,2,3}
*beginning, last = set
print(beginning, last)

my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7,8,9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
