# The proxy design pattern is similar to the decorator design pattern
#     It wraps functionality around the object creation
#     Uses additional layer of abstraction/protection when it comes to creating instances of classes
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Person(IPerson):

    def person_method(self):
        print('I am a person!')

# Creation of a proxy/'Middle Man' to create and handle person object 

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method() # Calls on the Person version and not on the ProxyPerson version

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()