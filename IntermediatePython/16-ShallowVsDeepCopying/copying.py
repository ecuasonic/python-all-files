org = 5
cpy = org # makes a new variable with same reference
cpy = 6 # will create a new variable, since integers are immutable
# org is 5, and cpy is now 6

# With mutable lists, we have to be careful
org = list(range(5))
cpy = org
cpy[0] = -10 # original org function is now [-10, 1, 2, 3, 4]

import copy
org = list(range(5)) # one level deep
cpy = copy.copy(org) # shallow copy 
cpy = org.copy()
cpy = list(org)
cpy = org[:]
cpy[0] = -10 # org is not affected
print(org)
print(cpy)

# Shallow Copy
org = [list(range(0,5)), list(range(5,10))]
cpy = copy.copy(org) # both the original and copy are changed when cpy is changed ; Shallow copying only applys with one level deep
cpy[0][1] = -10
print(org)
print(cpy)


# Deep Copy
org = [list(range(0,5)), list(range(5,10))]
cpy = copy.deepcopy(org) # deep copying applys to all levels 
cpy[0][1] = -10
print(org)
print(cpy)

#Shallow Copy Class - One layer
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 27)
p2 = p1 # p2 refers to the same reference as p1 ; they are not true copies
p2.age = 28 # changes both variables

p2 = copy.copy(p1) # shallow copy ; only one layer is copied
p2.age = 29


#Copy Class - Two layers
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex',55)
p2 = Person('Joe', 27)
company = Company(p1,p2)
company_clone = copy.copy(company) # shallow copy ; only the top layer is copied
company_clone.boss.age = 56 # changes both variables

company_clone = copy.deepcopy(company) # deep copy ; all layers are copied
company_clone.boss.age = 57 # only changes the copy version 


