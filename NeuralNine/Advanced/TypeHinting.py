# Python is a dynamically typed language, which means that we don't know what data types we're dealing with until runtime
'''
def myfunction(myparameter):
    if type(myparameter) == string:
        pass
    pass
'''
# We have a tool called 'mypy' which can check for so-called type hinting

def myfunction(myparameter: int) -> str: # 'python TypeHinting.py' acts like it suggests to input an integer type, but doesn't enforce it 
    # 'mypy TypeHinting.py' does enforce it and returns an error, otherwise
    # '-> str' means that the function is expected to return a string type object
    print(myparameter)
    return f'{myparameter + 10}'

#myfunction("Hello") ; ERROR
print(myfunction(10))

def otherfunction(otherparameter: str): # expects otherparameter to be string type object
    print(otherparameter)

otherfunction(myfunction(20))

# mypy is a tool that checks fro the consistency of type hinting

def dosth(param: list[int]):
    print(param)

#dosth([1,2,'a']) ; ERROR
dosth([1,2,3])
