# Numerical Operations
20^30 #10; bitwise XOR operation; 10100^11110 returns 01010 (10)
27&44 #8; bitwise AND operation; 011011^101100 returns 001000 (8)
44|21 #61; bitwise OR operation; 101100|010101 returns 111101 (61)
~21 #-22; bitwise NOT operation: ~10101 returns -10110 (-22); returns one more in magnitude but opposite sign;
~~20 #20

# Lists: collection data type, ordered, mutable, allows duplicates elements___________________________________________________________________________________________________________________
#list functions 
mylist = [4,5,3,7]
i = mylist.insert(0,-1) #None 
print(mylist) #[-1,4,5,3,7]
i = mylist.pop() #7; list is now [-1,4,5,3]
i = mylist.remove(-1) #None
print(mylist) #[4,5,3]
try:
    i = mylist.remove(7) #ERROR
except:
    pass
i = mylist.reverse() #None; much faster than lst[::-1]
print(mylist) #[3,5,4]
i = mylist.sort() #None
print(mylist) #[3,4,5]
i = sorted(mylist, reverse=True) #[5,4,3]; mylist.method() affects the list, regardless if the list is being assigned to another variable; sorted(mylist) doesn't affect the list 
print(mylist) #[3,4,5]
mylist.clear() #[]
#list creation, reassignment, and splicing
mylist = [0]*5 #[0,0,0,0,0]
mylist2 = [1]*5
new_list = mylist + mylist2 #[0,0,0,0,0,1,1,1,1,1]
mylist = [0,1,2,3,4,5,6,7,8,9,10,11,12]
a = mylist[1:10:2] #[2,4,6,8,10]; first two indexes are standard, last entry is the number of steps between 
a = mylist[-3:-1] #negative on the right are included, on the left are excluded; #[10,11]
a = mylist[::-1] #[12,11,10,9,8,7,6,5,4,3,2,1,0]
lo = ['a','b','c']
lc = lo.copy() #you can also use lc = list(lo) or lc = lo[:]
lc.append('d')
print(lc)
print(lo) 
lc = lo #both lists are assigned to the same list; change one will change the other
lc.append('d')
print(lc)
print(lo)
a = [1,2,3,4,5,6] #[1,2,3,4,5,6]
b = [i*i for i in a] #[1,4,9,16,25,36]; [expression for i in a]
mylist.extend([1,2,3])

# Tuple: collection data type, ordered, immutable, allows duplicate elements______________________________________________________________________________________________________________
t = "Max", 28, "Boston" #('Max', 28, 'Boston')
t = ('Max') #'Max'
lst = list(t) #['Max', 28, 'Boston']
t = tuple(["Max", 28, "Boston"]) #('Max', 28, 'Boston')
tuple[:-1] #tuple[slice(None, -1, None)]
i = t[slice(None,-1,None)] #['Max', 28]; the same as t[:-1:]
n = t.count(28) #1; works with lists
n = t.index(28) #1; records first-occurance index; can result in ERROR; works with lists
name, age, city = t #called 'unpacking'
tpl = (0,1,2,3,4)
i1, *i2, i3 = tpl #i1 = 0, i2 = [1,2,3], i3 = 4; works with lists
import sys
lst = [0,1,2,'hello',True]
tpl = tuple(lst)
print(sys.getsizeof(lst), 'bytes')
print(sys.getsizeof(tpl), 'bytes') #bytes of whats being stored
import timeit
print(timeit.timeit(stmt ="[0,1,2,3,4,5]", number=100))
print(timeit.timeit(stmt = "(0,1,2,3,4,5)", number = 100)) #the time it takes for the 'stmt' to run 'number' of times

# Dictionary: collection data type, key-value pairs, unordered, mutable, no repeats____________________________________________________________________________________________________________
dct = dict(name="Mary", age=27, city="Boston") #{'name':'Mary', 'age',27, 'city','Boston'}
try:
    value = dct["lastname"] #ERROR
except:
    pass
del dct["name"] #can't set entire line to another variable; dct = {'age':28, 'city':'New York'}
i = dct.pop("age") #27; dct = {'city':'New York'} #works with lists, but with index
dct = {'a':1, 'b':2, 'c':3}
i = dct.popitem() #('c',3); dct = {'a':1,'b':2}; removes and returns last item; takes no argument
for key in dct:
    print(key+':'+str(dct[key]))
keys = dct.keys() #dict_keys(['a', 'b'])
keys = list(keys) #['a','b']
values = dct.values() #dict_values([1,2])
values = list(values) #[1,2]
items = dct.items() #dict_items([('a',1),('b',2)])
items = list(items) #[('a',1), ('b',2)]
dct_cpy = dct #both dictionaries point to the same dictionary inside memory
print(dct_cpy)
print(dct)
dct_cpy['c'] = 3
print(dct_cpy)
print(dct)
dct_cpy = dct.copy() #you can also use dict(dct)
dct = {"name": "Max", "age":28, "email":"max@xyz.com"}
dct2 = dict(name="Mary", age=27, city="Boston")
dct.update(dct2) #{"name": "Mary", "age":27, "email":"max@xyz.com", "city":"Boston"}
dct = {(1,2):2}
try:
    dct = {[1,2]:2}
except:
    pass

# Sets: collection data type, unordered, mutable, no duplicates__________________________________________________________________________________________________________________________________________
myset = {1,2,3}
myset.clear()
myset = {1,2,3,1,2} #{1,2,3}
myset = set([1,2,3]) #{1,2,3}
myset = set('Hello') #{'o','H','l','e'}; Unordered
s = {} #<class 'dict'>
s = set() #<class 'set'>
myset.add(2) #inserts 2
myset.add(2) #no change
myset.remove('e') #removes 'e'
try:
    myset.removee('f')
except:
    pass
myset.discard(2) #removes 2; No ERROR if not in set
i = myset.pop() #randomly selects item to remove; returns discarded value
myset = {1,'b',5,'a',3,4} #the set will tend to be ordered, but sometimes isn't; the numbers appear to be always ordered
for x in myset:
    print(x)
if 5 in myset:
    print('yes')
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens) #combine both sets without duplication; {0,1,2,3,4,5,6,7,8,9}
i = odds.intersection(evens) #intesection between both sets; set()
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB) #A-B;(A)Inter(B*);{4,5,6,7,8,9}
diff = setA.symmetric_difference(setB) #[(A)Inter(B*)] Union [(A*)Inter(B)]; Includes elements that are not in both sets {4,5,6,7,8,9,10,11,12}
print(setA) #{1,2,3,4,5,6,7,8,9}; No change
setA.update(setB) #setA.union(setB) but actually changes the original set
setA.intersection_update(setB) #setA.intersection(setB) but actually changes the original set
setA.difference_update(setB) #setA.difference(setB) but actually changes the orginal set
setA.symmetric_difference_update(setB) #setA.symmetric_difference(setB) but actually changes the original set
a = setA.issubset(setB) #True; if all elements of setA is in setB then True; otherwise False
a = setA.issuperset(setB) #True; if all elements of setB is in setA then True; otherwise False
a = setA.isdisjoint(setB) #False; if the intersection is empty then True; otherwise False
setA = {1,2,3,4,5,6}
setB = setA #both sets point to the same set in memory
setB = setA.copy #or set(setA)
a = frozenset([1,2,3,4]) #immutable
print(a)
my_set = {a := 10, b := 2} #saves both a and b, assigns them to 10,2, then returns set

# Strings: collection data type, ordered, immutable, text representation___________________________________________________________________________________________________
my_string = 'I\'m a programmer'
my_string = "I'm a programmer"
my_string = '''Hello 
World''' # 'Hello\nWorld'
my_string = '''Hello \
World''' #Hello World'
ind = my_string.find('o') #4; only prints out the first instance; returns -1 if not found
count = my_string.count('o') #2
my_string = my_string.replace('World', 'Globe') #if not found, then return original
lst = my_string.split() #['Hello', 'Globe']; input is called 'delimiter'
my_string = ' '.join(lst) #'Hello Globe'
'''from timeit import default_timer as timer
lst = ['a']*400000
start = timer()
str = ''
for i in lst:
    str += i #'aaaaaa'; 9.9 sec
stop = timer()
print(stop-start)
start = timer()
str = ''.join(lst) #'aaaaaa'; 0.0048 sec; much much quicker than the other way
stop = timer()
print(stop-start)'''
# %, format(), f-Strings
var = "Tom"
my_string = "the variable is %s" % var #'the variable is Tom'; the '%s' serves as a placeholder
var = 3
my_string = "the variable is %d" % var #'the variable is 3'
var = 3.1431433214
mypercent = "the variable is %.3f" % var #'the variable is 3.14'; '%.3f' represents to get 3 decimal places
my_format = "the variable is {:.2f}".format(var) #'{:.2f} means 2 decimal places
my_format = "the variable is {} and {}".format(var, var) #places both in spots
my_f = f"the variable is {var*var} and {var}" #fastest and best way to do it; evalutated at runtime, so you can input math expressions

