# The factory desing pattern is one of many object-oriented design patterns
#     The goal of such an object-oriented design pattern is usually to increase the modularity, or the so-called seperation of concerns
#     Individual pieces of the program, such as the classes and modules, to mind their own business, do their job, and be very good at that job.

#     Very useful when we want to what particular instance we want to create during runtime
#     Useful in big applications where you have multiple classes and multiple python files and modules working together 

#     Not very useful in small applications, since they're increasing complexity and decreasing readability

from abc import ABCMeta, abstractstaticmethod # abc = 'abstract class'

class IPerson(metaclass=ABCMeta): # Person interface ; meta=ABCMeta basically means that this is an abstract class and we cannot create any instances of it

    @abstractstaticmethod
    def person_method():
        """ Interface Method """
        # An interface is when we know that we are going to have certain methods, but don't know yet which ones exactly
        # Each derived class seperately and distinctly overrides the method 
        #     In other words, the abstract method could do different things, depending on the branching class

# p1 = IPerson() ; ERROR

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student!")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher!")

s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()

# s1 = Student() ; ERROR

# Factory Design Pattern
class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()
        print("Invalid Type")
        return -1
    
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()