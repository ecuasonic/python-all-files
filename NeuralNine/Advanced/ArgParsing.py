# important for systems programming or developing network scripts that will be executed in the command line
# python myscript.py result.txt 
#     result.txt would be the input for the input() part of the python script

# python myscript.py -o test.txt -l DEBUG 

def myfunction(*args, **kwargs): # creates a boundless list of args and kwargs
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myfunction('hey', True, 19, 'wow', KEYONE='TEST', KEYTWO=7)




# The following sets conditions for a length requirement of args in the command line

import sys

print(sys.argv[0]) # file pathway here ; filename in command line 'python ArgParsing.py'
print(sys.argv[1]) # 'test' in "python ArgParsing.py test"
print(sys.argv) # ['ArgParsing.py', 'test', 'hello', 'new world'] in 'python ArgParsing.py test hello new\world'

# Usage: ArgParsing.py FILENAME
#     Argparsing.py is argv[0]
#     FILENAME is argv[1]

filename = sys.argv[1]
message = sys.argv[2]
with open(filename, 'w+') as f:
    f.write(message)




import sys
import getopt
# Usage: main.py -p 8080 -h local

filename = "test.txt"
message = "Hello"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
# only the things after the filename are processed
# The ":" after each 'f' and 'm' mean that a value is expected afterwards
# creates key, value tuple pairs between 'f' filename and 'm' message

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)

print(opts)
print(args)