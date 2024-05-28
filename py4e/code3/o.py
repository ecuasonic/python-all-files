import os
input('Enter a specified path: ') #'c:ecuas/onedrive/desktop/py4e' or 'c:/users/ecuas/onedrive/desktop/py4e'
try:
    print(os.listdir(input))
except:
    print('Didn\'t work. Try Again!')
