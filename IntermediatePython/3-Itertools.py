# itertools: ____________________________________________________________________________________________________________________________________________________________________________________________________
#     collection of tools for handling iterators, which are data types that be used in a loop
#     product, permutations, combinations, accumulate, groupby, and infinite iteration
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) #<itertools.product object at 0x000001FADB298980>
prod = list(prod) #[(1,3),(1,4), (2,3), (2,4)]; Includes every possible combination with one element from both sets 
prod = list(product(a,b,repeat=2)); #[(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)];
#Includes every possible combination with two elements from both sets; repeating items allowed


from itertools import permutations
a = [1,2,3]
perm = permutations(a) #<itertools.permutations object at 0x00000204AB2C2E30>
perm = list(perm) #[(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)] #returns all possible arrangements of the list's items
perm = list(permutations(a,2)) #[(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)] #returns all possible length-2 arrangements 


from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) #<itertools.combinations object at 0x00000286A13C6E80>; second input is mandatory
comb = list(comb) #[(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]; returns all possible length-2 unordered groups with no repeating item
comb = list(combinations_with_replacement(a,2)) #[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]; returns all possible length-2 unordered groups with repeating item


from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a) #<itertools.accumulate object at 0x000001D184AF4380>
acc = list(acc) #[1,3,6,10]; accumulates the item value as tranversing the list


import operator
acc = list(accumulate(a, func=operator.mul)) #[1,2,6,24]; multiplies the item value as transversing the list
a = [1,2,5,3,4,10]
acc = list(accumulate(a, func=max)) #[1,2,5,5,5,10]; if the next items are less than the one before it, then it becomes the greater value
acc = list(accumulate(a, func=min)) #[1,1,1,1,1,1]; if the next items are more than the one before it, then it becomes the smaller value


from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obj = groupby(a,key=smaller_than_3) #<itertools.groupby object at 0x000001C5E2AECDB0>
#group_obj = list(group_obj) #[(True, <itertools._grouper object at 0x0000022EC7584790>), (False, <itertools._grouper object at 0x0000022EC7584850>)]
for key, value in group_obj:
    print(key,list(value)) #True [1,2] // False [3,4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value)) #True [1,2] // False [3,4]
persons = [dict(name='Tim',age=25), dict(name='Dan',age=25), dict(name='Lisa',age=27), dict(name='Claire',age=20)]
group_obj = groupby(persons, key=lambda x: x['age'])
for key,value in group_obj:
    print(key,list(value)) #25 [{'name':'Tim', 'age':25}, {'name':'Dan', 'age':25}] // 27 [{'name':'Lisa', 'age':27}] // 20 [{'name':'Claire', 'age':20}]


from itertools import count, cycle, repeat
for i in count(10): #10 is the start value; count acts infinitely, it is basically range(infinity) but starts at 10 in this case (10,11,12...)
    print(i)
    if i==15:break
a = [1,2,3]
for i in cycle(a): #[1,2,3,1,2,3,1,2,3,...]
    print(i)
    if i == 3: break
a = [1]
for i in repeat(a,5): #[[1],[1],[1],[1],[1]]; repeats list (a) 5 times; if second input is not included, then it will make an infinite loop
    print(i)