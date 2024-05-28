# JAVAdocs are a special kind of comment that you write above a function or class

def myexpo(num1, num2):
    '''
    This function takes one number to the power of another number and returns the result!

    :param num1: This is the base
    :param num2: This is the exponent
    :return: The result of the calculation
    '''
    return num1**num2

print(myexpo(3,2)) # Shows the documentation above
help(myexpo)
print(myexpo.__doc__)