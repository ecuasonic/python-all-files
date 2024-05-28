# Multiple classes that inherit from the same interface or parent class and one of those can consist of many of the others 
#     Ex: One region can consist of many sub-regions and those sub-regions can consist of other sub-regions
# Creates a hierarchy and a tree-like structure 
#     Increases flexibility and easier to use

from abc import ABCMeta, abstractclassmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractclassmethod
    def __init__(self, employees):
        """ implement in child class """

    @abstractstaticmethod
    def print_department():
        """ implement in child class """

class Accounting(IDepartment):
    
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()