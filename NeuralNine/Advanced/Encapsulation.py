class Person:

    def __init__(self, name, age, gender):

        self.__name = name # Private attributes ; Can only accessed within the class
        self.__age = age
        self.__gender = gender

    @property # Turns this into a property ; Not callable at all 
    def Name(self): # getter
        # can be accessed by p1.Name, which would return self.__name
        return self.__name
    
    @Name.setter
    def Name(self,value): # setter ; the same method name as the getter method for name ; used to change the value of self private attributes
        # p1.Name = 'Bob'
        if value == 'Bob':
            self.__name = "Default Name" 
        else:
            self.__name = value

    @staticmethod # method with no parameters ; can be called by both the class and objects of the class
    def mymethod():
        print("Hello world!")

    # There is no method overloading in Python ; There can't be two methods with same names
    #     The combination of @property on Name() and @Name.setter overrides this 

p1 = Person("Mike",20,'m')
print(p1.Name)

p1.Name = "Bob" # the "@Name.setter" allows this ; This only inputs "Bob" as an argument
# But doesn't assign p1.Name to "Bob" 
print(p1.Name)

Person.mymethod()
p1.mymethod()
# Both of these calls do the same thing