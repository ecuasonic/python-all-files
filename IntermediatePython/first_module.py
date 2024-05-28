
print(f"First Module's Name: {__name__}") #'First Module's Name: __main__'

#whenever python runs a file, at first (before running the code), it sets a few special variables: __name__ is one of those variables
#   __main__ is assigned to __main__ when python runs a python file directly ; we are currently running the file directly
#   whenever we import a module, 
#       *******__name__ is assigned to the name of the file, within the imported file*******

#this is helpful for running code only when run either directly or through module import

def main():
    print('This^ module was directly run by Python')

def notMain():
    print('This^ module was imported')

if __name__ == '__main__': #runs if directly run by python ; doesn't if imported
    main()
else:
    notMain()