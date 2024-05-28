import first_module #'First Module's Name: first_module'
#the first_module file is no longer being directly run by Python, but instead imported 

#first_module.main() ; runs the main() method in first_module

print(f"Second Module's Name: {__name__}") #'Second Module's Name: __main__'
#Only __name__ called in the first_module will be assigned to 'first_module'
#__name__ run here will be assigned to '__main__'