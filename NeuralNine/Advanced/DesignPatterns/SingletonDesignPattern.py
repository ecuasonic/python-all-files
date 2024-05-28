# Singleton Design Pattern
#     Ensures that a class has only one instance and provides a global point of access to that instance
from abc import ABCMeta, abstractstaticmethod
# Abstract Base Classes (abc)
# Abstract methods are methods that have a declaration in the base class but don't contain any implementation
#     They must be overriden (implemented) in the derived classes

class IPerson(metaclass=ABCMeta):
    # Abstract base class with a static abstract method 'print_data()'
    #     This means any class inheriting from 'IPerson' must implement the 'print_data()' method as a static method

    @abstractstaticmethod
    def print_data():
        """ implement in child class """

class PersonSingleton(IPerson):

    __instance = None # private class-wide variable 

    @staticmethod 
    # Used to define a static method within a class
    # Belongs to the class and not to the instance of the class
    #     Cannot access or modify instance-specified data or attributes
    # Does not receive any special first args ('self') and behaves like a regular function with no implicit reference to the instance
    # Commonly used to define methods that don't need access to instance-specific data and perform general utility operations related to the class
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self 

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

# p2 = PersonSingleton("Bob", 25) ; ERROR
p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()