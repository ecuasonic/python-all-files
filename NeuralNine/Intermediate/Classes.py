class Person:

    amount = 0 # Class-wide variable ; accessible by "Person.amount"

    def __init__(self, name, age): #Constructor
        self.name = name #Attributes
        self.age = age 
        Person.amount += 1

    def __str__(self): # print(p1)
        return (f"Name: {self.name}, Age: {self.age}")

    def __del__(self): #Destructor
        Person.amount -= 1
        print("Person object deleted") #Printed at the end, because after program runs, the objects are deleted

    def get_older(self, years):
        self.age += years

p1 = Person("Richard", 20)
p2 = Person("Bob", 500)
p3 = Person("M", 20)
p1.get_older(20)


class Worker(Person):
    
    def __init__(self,name,age,salary):
        super().__init__(name, age) # super method runs the __init__ of the first parent class with identical parameter names
        self.salary = salary

    def __str__(self):
        text = super().__str__() # uses the text output for __str__ in Person parent class
        text += f", Salary {self.salary}" # adds this section to text
        return text
    
    def calc_yearly_salary(self):
        return self.salary*12
    
    

w1 = Worker('Merg', 34, 79000)
print(w1)
print(w1.calc_yearly_salary())

del p1,p2,p3
del w1

# Operator Overloading - Not every programming language allows this (Java doesn't, but Python does)
#      Defines what happens when adding two objects together 
class Vector:

    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'
    
    def __del__(self):
         print("Vector bject deleted")

    
v1 = Vector(1,2)
v2 = Vector(0,1)
v3 = v1 + v2
print(v3)