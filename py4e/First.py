#Chapter 1__________________________________________________________________________________________________________________________________________________________________

print('hello from a file');

x = 2
print(x);
x = x + 2
print(x);

while n > 0:
    n = 5
    print(n)
    n = n - 1
print('Blastoff')

x = 2**4
x = x%3   #x(mod3)


#Chapter 2: Variables__________________________________________________________________________________________________________________________________

#Operator Precedence Rules: (), */, +-, left to right. * and / have the same level of precendence, just that they are read from left to right (same with + and -)
#division always outputs floating number in python3 (not in python2)

# type(x) : returns the input's variable type
# float(int) : converts integer to floating number
# int(x) : converts floating number to integer; converts number strings into integers
# n = input(str) : returns str, waits for input from user, then assigns input to the variable n as a string
# print(str, n) : returns "str n"; the comma automatically inserts the space between str and n


#Chapter 3: Conditional Execution______________________________________________________________________________________________________________________

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

#Comparison Operators: <, <=, ==, >=, >, !=
#Indentation errors may occur if tabs and spaces are mixed up; Python only read 4 spaces; Atom automatically assigns a tab space into 4 spaces.

x = 4
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')
#if the "elif" runs, then the "else" doesn't

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')
#if the code in "try" works, then the "except" is skipped. However, if the "try" fails, then it jumps to "except" section


#Chapter 4: Functions__________________________________________________________________________________________________________________________________

def thing():
    printt('Hello')
    print('Fun')
thing()
print('Zip')
thing()

big = max('Hello world')
print(big) #returns "w"
tiny = min('Hello world')
print(tiny) #return

def greeting():
    print("Hello")
    print("How are you")

def greet(lang):
    if lang == 'es':
        return('Hola')
    elif lang == 'fr':
        return('Bonjour')
    else:
        return('Hello')

#"return" keyword outputs a value and stops the rest of the code; the value can be assigned to a variable
#    i"nstead of being printed out into the console

def greet():
    return "Hello"
print(greet(), "Gleen")
print(greet(), "Sally")

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print(x)

#Chapter 5: Loops and Iteration_____________________________________________________________________________________________________________________________

n = 5
while n > 0:
    print(n)
    n = n - 1
print ('Blastoff!')
print(n)

#be careful with infinite Loops and unused loops

#the "break" statement ends the current loop and jumps to the statement immediately following the loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#the "continue" statement ends the current iteration and jumps to the top of the loop and starts the next iteration
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

#indefinite loop: while; definite loop: for
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends = ['Joe', 'Sal', 'Gleen']
for person in friends:
    print('Happy New Year:', person)
print('Done!')

temp = -1;
print('Before', temp)
for i in [99,41,12,3,73]:
    if i < temp:
        temp = i
    print(temp, i)
print('After', temp)

# you can count, add up, and filter values over iterations in a For loop

found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#"None" is a constant value unlike boolean and integers, and can be assigned to all types if looked for
#    "None" is detected through the use of "is" as if to say "=="
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = values
    elif value < smallest:
        smallest = values
    print(smallest, value)
print('After', smallest)
#Does the order of inequality matter?
#"is" asks for equallity in both type and value, while == asks for the equality in value. Both "is" and "is not" are logical operators
#Use "is" in boolean and none types. Avoid using in integers, floats, or strings, although it may work sometimes, but not between each other.

#Chapter 6: Strings__________________________________________________________________________________________________________________________________________________________

#strings start at the index of 0
#We can get at any single charater in a string using an index specified in square brackets
str = "Hello"
e = str[1];

#the function len() gives us the length of a string
fruit = 'banana'
print(len(fruit))

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#a string can also act as a list in terms of for loops
fruit = 'banana'
for letter in fruit:
    print(letter)

#slicing strings: we can also look at any continous section of a string using a colon operator
#    the first index is included, while the ending index is not
s = 'Monty Python'
print(s[0:4]) #prints out "Mont"

#even if the ending index is beyond the length scope of the string, there is still no error
print(s[6:20]) #prints out "Python"

#not including the starting or ending index assumes that the rest of the string is outputed
print(s[:2]) #prints out "Mo"

#The "in" keyword can also be used to check to see if one string is "in" another string
fruit = 'banana'
'n' in fruit #returns True
'nan' in fruit #returns True
if 'a' in fruit:
    print('Found it!')
#in is used as a logical operator in this case, instead of in a for loop

#String comparison depends on the computer; Upper case > lower case for the most part, and a > b > c >...
if word == 'banana':
    print('All right, bananas')
if word < 'banana':
    print('Your word, ' + word + ', come before bananas.')

#string library; there are built-in string functions that operate on strings, these functions don't change the value of the inital string
greet = 'Hello Bob'
zap = greet.lower()
print(zap)                  #prints out 'hello bob'
print('Hi There'.lower())   #prints out 'hi there'
#a new string is returned
#this is an example of a method call, where the function doesn't change the object, but returns a new one
#len() is not object-orientated, while str.length() is

#you can find all the methods calls possible for strings
stuff = 'Hello world'
type(stuff)
dir(stuff)

str = ''
str.capitalize()
str.center(width[, fillchar])
str.startswith(suffix[, start[, end]])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()

fruit = 'banana'
pos = fruit.find('na')

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')

greet = '     Hello Bob    '
greet.lstrip()
greet.rstrip()
greet.strip()

#code used to look for and return certain splices
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
atpos = data.find('@')
appos = data.find('', atpos)
host = data[atpos+1, : appos]
print(host)

#Chapter 7: Reading Files__________________________________________________________________________________________________________________________________________

#open() function allows us to tell python which file we are going to work with
#    open() returns a "file handler," which is a function used to perform operations on the file
#    similar to how "File -> Open" in a Word Processor
#    open() doesn't read the file, it just makes it possible to be able to read the File

#handle = open(filename, mode)
#mode = 'r' if read or 'w' if writing; mode is optional, 'r' is the default
fhand = open('mbox.txt','r')

#a handle is like an opening/channal between python program and the file

#The newline Character: \n indicates when a line ends in a string; similar to pressing enter in Word
stuff = 'Hello\nWorld!'
stuff = 'X\nY'
#python automatatically places a \n in the end of the string
#\n counts as a single character, when len(stuff)=3 is calculated;
#text files have newlines at the end of each line

#a file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
#    we can use the for statement to itterate through a sequence
xfile = open('mbox.txt')
for str in xfile:
    print(str)

fhand = open('mbox.txt')
count = 0
for str in fhand:
    count = count+1
print('Line Count:',count)

#We can read the whole file(newlines and all) into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#Searching througha a file
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

#the newlines aren't thrown away after each line; then the print statement adds a new \n each time
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#rstrip() removes any whitespace in the string (whitespace is anything that is not printed out, such as the \n)
#    important**

#can use continue to perform the same task
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#can use "in" to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#can set fhand to be input
fname = input('Enter the file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject liense in',fname)

#bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:'.fname)
    quit()
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject liense in',fname)

#chapter 8: Lists_______________________________________________________________________________________________________________________________

#a collection allows us to put many values in a single 'variable'
friends = ['Joe','Gleen','Sal']
rand = [1,2,'hello']
rand2 = [2,3,[3,4],'yes']
empt = []

for i in rand:
    print(i)
print('Done!')

#just like strings, we can get at any single element in a list using an index specified in []
print(rand[1])
print(friends[0])

#strings are 'immutable' - we cannot change the contents of a string - we must make a new string to make any changes
#    lists are 'mutable' - we can change the content of the lists
rand[2] = 'hello'
friends[0] = 'Bob'

#len() can also be used on lists
print(len(rand))

#range() function returns a list of numbers that range from zero to one less than the parameter
#   range(2) = [0,1]
print(range(len(rand)))

#two different loops doing the same thing
for item in rand:
    print('Hello',item)

for i in range(len(rand)):
    item = rand[i]
    print('Hello',item)

#concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a+b #c = [1,2,3,4,5,6]

#lists can be sliced using ":" similar to strings; "up to but not including"
c[1:3]
c[:3]

#list methods
x = list()
type(x)
dir(x)
#append, count, extend, index, insert, pop, remove, reverse, sort

#building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) #['book', 99]

#you can use the "in" operator in a list, similarly used in a string; output is a boolean; also "not in"
some = [1,9,21,10,16]
9 in some
15 in some

#A list can be sorted mutabily (the list itself changes and doesn't create another list, unlike for strings)
friends = ['Joe','Gleen','Sal']
friends.sort()
print(friends[1])

#built-in functions and lists
nums = [2,3,1,3,6]
print(len(nums))
print(max(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#two different programs to calculate average (second one uses more memory than the first)
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print('Average:',average)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:',average)

#split() breaks a string into parts and produces a list of strings
abc = 'with three words'
stuff = abc.split() #['with','three','words']
print(len(stuff)) #3
print(stuff[0]) #with

#the split() function splits the strings whereever there is whitespace between text
#a demiliter can be used to split strings based on the demlimiter; str.split(delimiter)
line = 'A lot             of spaces'
etc = line.split()
print(etc) #['A','lot','of','spaces']

line = 'first;second;third'
thing = line.split()
print(thing) #[first;second;third]

thing = line.split(;)
print(thing) #['first','second','third']

#the double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#using "or" in if lines
if len(wds) < 3 or wds[0] != 'From':
    continue
#the order of the "or" matters in terms of which python checks first. If the first option blows up but the second wouldn't,
#    then you make the second option as the first. If the first part is true, then the second part is not evaluated

#Chapter 9: Dictionaries____________________________________________________________________________________________________________________________

#a list is like a linear collection of values that stay in order
#a dictionary is a "bag" of values, each with its own label
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse) #{'money' : 12,'candy' : 3, 'tissues' : 75}
purse['candy'] = purse['candy'] + 2

ooo = {}

#it is an error to reference a key which is not in the dictionary
#we can use the "in" operator to see if a key is in the dictionary
ccc = dict()
print(ccc['csev'])
'csev' in ccc #False

#new name / name counter
counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen', 'csev']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) #{'csev' : 2,'cwen' : 2,'zqian' : 1}

#The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there
#    is so common that there is a method called get() that does this for us
#these two programs do the same time: look for 'name' in counts; returns the value assosiated with name and 0 is not.
#counts.get(name,0) includes counts[name] in terms of capability, but is more powerful in that there is a value returned when name doesn't exist
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get('csev', 0) #2
x = counts.get('no',0) #0

#simplified counting with get() #idiom: retrieve/create/update counter all in one line
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

#definite loops and dictionaries
#a for loop in a dictionary goes through all of the keys and looks up the values
counts = {'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])

#retrieving lists of keys and values
print(list(counts)) #['jan','chuck','fred']
print(counts.keys()) #['jan','chuck','fred']
print(counts.values()) #[100,1,42]
print(counts.items()) #[('jan',100),('chuck',1),('fred',42)] #tuples

#Bonus: Two iteration variables #possible with tuples
for aaa,bbb in counts.items():
    print(aaa,bbb)

#Chapter 10: Tuples_______________________________________________________________________________________________________________________________________________

#tuples are another kind of sequence that functions much like a list
#    they have elements which are indexed starting at 0

x = ('Glenn', 'Sal','Joe')
print(x[2]) #Joe
y = (1,9,2)
print(y)
print(max(y))

for iter in y:
    print(iter)

#Similar to a string, but not to a list, tuples are "immutable"
#    you cannot alter its contents
y = (5,4,3)
y[2] = 0 #error

#they are not modifiable to promote effciency and occupy less storage

#any object method that is possible with a list and modifies it, such as .sort(), .append(), .reverse() can't be used with tuples
#only .count() and .index() work for tuples

#tuples and assignment
(x,y) = (4,'fred')
print(y) #fred
(a,b) = (99,98)
print(a) #99

#tuples and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
tups = d.items()
print(tups)

#tuples are comparable
#    compares the first pair that isn't equal to each other, then doesn't compare the rest (<,>)
#    tuples are equal when all corresponding pair components between the tuples are true (<=,>=,==)
(0,1,200000) < (0,3,4) #True
('Jones','Sally') < ('Jones','Sam') #True

#we can take advantage of the ability to sort a list of tuples to get a sorted version of dictionary
#we can sort the dictionary by key using items() method and sorted() function
d = dict()
d['a'] = 10
d['b'] = 1
d['c'] = 22
d.items()
sorted(d.items)

#using sorted()
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t) #[('a',10),('b',1),('c',22)]
for k,v in t:
    print(k,v)

#sort by values instead of keys
c = d
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp) #[(10,'a'),(1,'b'),(22,'c')]
tmp = sorted(tmp, reverse=True)
print(tmp) #[(22,'c'), (10,'a'), (1,'b')]
#in command prompt (k,v) and k,v in the for loop does the same thing, in this case
#.sort() and .reverse() can be used on tmp

#top 10 most common words:
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse = True)
for val, key in lst[:10]:
    print(key,val)

#even shorter version
print(sorted([ (v,k) for k,v in counts.items() ])) #lst = ['expression' for 'item' in 'list']
#the inner portion([ (v,k) for k,v in c.items()]) is called list comprehension, which creates a dynamic list

#Chapter 11: Regualar Expressions____________________________________________________________________________________________________________________

#also referred to as "regex" or "regexp," this provides a concise and flexible means for matchiing strings of text,
#    such as particular characters, words, or patterns of characters. A regualar expression is written in a formal language
#    that can be interpreted by a regular expression processor
#Really smart "Find" or "Search"
#Very powerful but quite cryptic

#Regular Expression Quick Guide:
^ #Matches the beginning of a line
$ #Matches the end of the line
. #Matches any character
\s #Matches whitespace
\S #Matches any non-whitespace character
* #Repeats a character zero or more times
*? #Repeats a character zero or more times (non-greedy)
+ #Repeats a character one or more times
+? #Repeats a character one or more times (non-greedy)
[aeiou] #Matches a single character in the listed set
[^XYZ] #Matches a single character not in the listed set
[a-z0-9] #The set of characters can include a range
( #Indicates where string extraction is to start
) #Indicates where string extraction is to end

#progamming language that is character-based, not line-based or keyword-based
#    the characters mean something

#before you can use regular expressions in your programs, you must import the library using "import re"
#you can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
#you can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]

#using re.search() like find()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') != -1: #line.find('From:') returns the index of the input str within the outer string (-1 if not in string)
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)

#using re.search() like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'): #line.startswith returns boolean
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)

#Wild-Card Characters
#    The dot(.) character matches any character
#    The asterisk(*) character repeats "any number of times"

re.search('^X.*:',line)
#Matches any line that begins with "X," and a splice that ends with ":" (doesn't have to be the very last character in the line)
#    there are character (both whitespace and non-whitespace) between X and :, and there is at least zero characers in between 'X' and ':'

re.search('^X-\S+:', line)
#Matches any line that begins with "X-," and a splice that ends with ":" (doesn't have to be the very last character in the line)
#    there are only non-whitespace characters between 'X-' and ':', and there is at least one non-whitespace character in between 'X-' and ':'

#re.search() returns a True/False  depending on whether the string matches the regular expression
#if w3 actually want the matching strings to be extracted, we use re.findall()
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y) #['2','19','42']
#re.findall('[0-9]+',x) means to find all splices of 1 or more digit numbers
y = re.findall('[AEIOU]+', x)
print(y) #[]

#Greedy matching: if the findall/search re methods is able to choose between overlapping short and long strings, it will choose the larger one (greedy)
import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y) #['From: Using the :']

#Non-Greedy Matching: perfers the shorter of the string
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y) #['From:']

#Fine-Tuning String Extraction (Greedy vs Non-Greedy)
str = 'From stephen.marquard@uct.ac.za Sat Jan 5'
y = re.findall('\S+@\S+',str)
print(y) #['stephen.marquard@uct.ac.za']
z = re.findall('\S+?@\S+?', str)
print(z) #[d@u] ; outputs the shortest string possible when non-greedy

#parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.find('^From (\S+@\S+)',x)
print(y) #['stephen.marquard@uct.ac.za'] ; much more precise than without

#How we first searched and extracted information from strings
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
atpos = data.find('@')
print(atpos) #21
sppos = data.find(' ',atpos)
print(sppos) = 31
host = data[atpos+1 : sppos]
print(host) #uct.ac.za

#How to do it with the double split pattern
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1]) #uct.ac.za

#How to do it with regualar expressions (regex)
import re
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
host = re.findall('@ ([^ ]*)', data)
print(host) #['uct.ac.za']

#Better regex version
import re
data = 'From stephen.marquard@uct.ac.za Sat Jan 5'
y = re.findall('^From .*@([^ ]*)', data)
print(y) #['uct.ac.za']

#searches for maximum number in txt file, with restrictions
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

#escape character: if you want a special regular expression character to just behave normally, you prefix it with "\"
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y) #['$10.00']


#Random Module Import________________________________________________________________________________________________________________________________________________
import random

ints = list()
temp = None
for i in range(100):
    temp = random.randint(0,10)
    ints.append(temp)
print('Largest value:', max(ints)) #Largest value: 10
print('Smallest value:',min(ints)) #Smallest value: 0

import random

def GuessingGame():
    num = random.randint(0,10)
    guess = input('Guess a number between 0 and 10, inclusive: ')
    t = True
    while t == True:
        try:
            if int(guess) == num:
                print('You\'ve guessed the number!:',num)
                t = False
            elif int(guess) > num:
                guess = input('You guessed too high! Try again! Guess another number: ')
            else:
                guess = input('You guessed too low! Try again! Guess another number: ')
        except:
            guess = input('You did not give me a number! Try again! Guess a number: ')

GuessingGame()

import random

def GuessingGame():
    num = random.randint(0,100)
    guess = input('Guess a number between 0 and 100, inclusive: '))
    while True:
        try:
            if int(guess) == num:
                print('You\'ve guessed the number!:',num)
                break                                                                        #break also serves the same function as setting t = false, and much cleaner in programming ide space
            elif int(guess) > num:
                guess = input('You guessed too high! Try again! Guess another number: ')
            else:
                guess = input('You guessed too low! Try again! Guess another number: ')
        except:
            guess = input('You did not give me a number! Try again! Guess a number: ')

GuessingGame()

#Chapter 12: Networked Programs________________________________________________________________________________________________________________________________

#Transport Control Protocol (TCP)
#    Provides a nice reliable pipe between the client (source) and server (destination)

#TCP Connections / Sockets
#    "In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet"
#    The connection is the socket

#TCP Port Number
#    Analogous to phone call extension numbers
#    A port is an application-specfic or proces-specific softeware communications endpoint
#    It allows multiple networed applications to coexist on the same server
#    Ex: Incoming E-Mail is assigned to port 25 ; Login is assigned to port 23 ; HTTP (80) ; HTTPS (443); DNS (53) ; SSH (22)
#        Look up "List of TCP and UDP port numbers"

# "www.lasi-asia.org:8080/wp/"
#    ":8080" means that it's a web server running on a "non-standard" port other than the official 80 or 443 port

#python has built-in support for TCP Sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket, but doesn't associate it ; socket that goes across the Internet ; continous series of char that come one after another
mysock.connect(('data.pr4e.org', 80)) #analogous to dialing a phone number and extension number, but not speaking yet ; this line of code could return an error

#Application Protocol
#    Ex: Mail, World Wide Web

#HTTP - Hypertext Transfer Protocol
#    Set of rules to allow browsers to retrieve web documents from servers over the Internet
#    Dominant Application Layer Protocol on the Internet
#    Invented for the Web - to Retrieve HTML, Images, Documents, etc.
#    Extended to be data in addition to documents - RSS, Web Services, etc. - Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the Connection

#Uniform Resource Locator (URL): "http://www.dr-chuck.com/pagel.htm"
#    "http://" is the protocol
#    "www.dr-chuck.com" is the host
#    "/pagel.htm" is the document

#Getting Data From the Server
#    Each time the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request for the contents at a specified URL
#    The server returns the HTML document to the Browser which formats and displays the document to the user

#HTML (Hypertext Markup Language)

#Internet Standards
#    The standards for all of the Internet protocols (inner workings) are developed by the Internet Engineering Task Force (IETF) ; 'www.ietf.org'
#    Standards are called "RFCs" - "Request for Comments"

#Making an HTTP request
#    Connect to the server like "www.dr-chuck.com"
#    Request a document (or the default document)
#        "GET http://www.dr-chuck.com/page1.htm HTTP/1.0"
#        "GET http://www.mlive.com/ann-arbor/ HTTP/1.0"
#        "GET http://www.facebook.com HTTP/1.0"

#telnet www.dr-chuck.com 80
#Trying 74.208.28.177
#Connected to www.dr-chuck.com.Escape charcter is '^J'.
#GET http://www.dr-chuck.com/page1.htm HTTP/1.0
telnet www.dr-chuck.com 80 ; GET http://www.dr-chuck.com/page1.htm HTTP/1.0

#An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #string to byte array
mysock.send(cmd)
while True:
    data = mysock.recv(512) #ask up to 512 characters
    if(len(data) < 1): #end of file
        break
    print(data.decode())
mysock.close()

#ASCII (American Standard Code for Information Interchange)
#    Each character is represented by a number between 0 and 256 stored in 8 bits of memory
#        The first 128 characters are familar but then rest aren't
#    We refer to 8 bits of memory as a "byte"
#    The ord() fucntion (ordianal position) tells us the numeric value of a simple ASCII character
#        Has to do with sorting and comparing strings together
print(ord('H'))
print(ord('e'))
print(ord('\n'))

#Unicode includes billions of characters from any language and large enough to have any character possible

#Multi-Byte Characters
#    To represent the wide range of characters computers must handle we represent characters with more than one byte
#        UTF-16 - Fixed length - Two Bytes (Halt Unicode)
#        UTF-32 - Fixed length - four Bytes (Full Unicode)
#        UTF-8 - Dynamic Length - 1-4 Bytes
#            Upwards compatible with ASCII (1 Byte)
#            Automatic detection between ASCII and UTF-8
#            UTF-8 is recommended practice for encoding data to be exchanged between systems

#In python 3, unicode and strings are the same, and bytes are another type
#In python 2, bytes and strings are the same, and unicode is another type

#When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

#Using urllib in Python
#    Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file
#    You can treat it like a file, but remember to decode
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #makes the connections, encodes the GET request, and retrieves headers; returns object that looks like a file handle
for line in fhand:
    print(line.decode().strip()) #we have to decode them

#Find most common words using urllib
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro.txt')
counts = dict()
for line in fhand: #type(line) is bytes
    words = line.decode().split() #decode() converts bytes to string
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#Reading Web Pages
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://wwww.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
#<h1>The First Page</h1>
#<p>
#If you like, you can switch to the
#<a href="http://www.dr-chuck.com/page2.htm">
#Second Page</a>.
#</p>

#What is Web Scraping?
#    When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages
#    Search engines scrape web pagegs - we call this "spidering the web" or "web crawling"

#Why Scrape?
#    Pull data - particularly social data - who links to who?
#    Get your own data back out of some system that has no "export capability"
#    Monitor a site for new information
#    Spider the web to make a database for a search engine

#Scraping Web Pages
#    There is some controversy about web page scraping and some sites are a bit snippy about it
#    Republishing copyrighted information is not allowed
#    Violating terms of service is not allowed

#Parsing HTML is difficult
#    You can right RegEx expresions, but broken HTML will not be ignored; there are many ways to mess up anchor tags
#    BeautifulSoup does this and compensates for the broken HTML
import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read() #read the entire thing #in bytes
soup = BeautifulSoup(html, 'html.parser') #repairs HTML if needed #has decode() within #in string
#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#*****************IMPORTANT********************
#the .py file running BeautifulSoup has to be stored in a folder that is of the same level as bm4, in order for BeautifulSoup() to work

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors; SSL certificate is not in python's official list
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#Chapter 13: Using Web Services____________________________________________________________________________________________________________________________________________________________________________________________________________________

#Data on the Web
#    With HTTP Request/Response wll understood and well supported, there was a natural move toward exchanging data between programs using these protocols
#    We needed to come up with an agreed way to represent data going between applications and across networks
#    There are two commonly used formats: XML (eXtensible Markup Language; .docx) and JSON (JavaScript Object Notation; Simpler, but not as descriptive)

#sending information from one program to the network requires an agreed upon format/protocol independent of any other programmiing language
#    Serialization formats
#    This protocol is called "Wire Protocol" - What we send on the "wire"
#    Python Dictionary is Serialized into "Wire Protocol," then De-Serialized to Java HashMap
#    XML "Wire Protocol" includes <person> <name> Chuck </name> <phone> 303 4456 </phone> </person>

#XML***************************************
#    Primary purpose is to help information systems share structured data
#    It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

#XML Terminology
#    Tags indicate the beginning and ending of elements
#    Attributes - Keyword/value pairs on the opening tag of XML
#    Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

#XML Basics
#    <person> "Start Tag"
#    </person> "End Tag"
#    Chuck "Text Content"
#    type = "intl" "Attribute"
#    <email hide = "yes"/> "Self-Closing Tag"

#    <person>
#     <name>Chuck</name>
#     <phone type = "intl">
#      +1 734 303 4456
#     </phone>
#     <email hide = "yes"/>
#    </person>

#Mistakes in XML are more severe than in HTML, they may not be understood
#Line ends do not matter. Whitespace is generally discarded on text elements. We indent only to be readable.

#XML can be treated as a tree graph of nodes; the most outer tag is called the root tag of the tree, and there can only be one root tag
#    any nodes extending from another node are called "children" of the other node
#    Text, Attributes can also be children of a node for which they are affecting
#    You can have multiple attributes associated with a node, but only one text node


#XML can also be seen as paths
#    "/a/b X"
#    "/a/c/d Y"
#    "/a/c/e Z"

#XML example #1
import xml.etree.ElementTree as ET #ET can be used instead of xml.etree.ElementTree for object methods such as ET.fromstring()
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''
type(data) #<class 'str'>
tree = ET.fromstring(data) #This part of the code can return error; it tells where the XML error is with respect to the beginning of the XML string
print(tree) #<Element 'person' at 0x000002CAF1D355D0>
type(tree) #<class 'xml.etree.ElementTree.Element'>
print('Name:', tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))

#XML example #2
import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
print(stuff) #<Element 'stuff' at 0x000001DA9C2E53A0>
type(stuff) #<class 'xml.etree.ElementTree.Element'>
lst = stuff.findall('users/user') #find all user nodes that branch off the users node
print(lst) #[<Element 'user' at 0x000001DA9C2E5440>, <Element 'user' at 0x000001DA9C2E5530>]
type(lst) #<class 'list'>
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text) #text
    print('id:', item.find('id').text) #text
    print("#:", item.get('x')) #attribute

#XML Schema: Describing a "contract" as to what is acceptable XML
#    Description of the legal format of an XML document
#    Expressed in terms of constraints on the structure and content of documents
#    Often used to specify a "contract" between systems
#        "My system will only accept XML that conforms to this particular Schema"
#    If a particular piece of XML meets the specification of the Schema, it is said to "validate"
#    Similar to RFCs, but the scope is between two applications

#XML Validation
#    XML Document(input) and XML Schema Contract(input) are sent into an XML validator to see if XML doc follows Contract
XmlDoc = '''
<person>
    <lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person>'''
XmlContractContract = '''
<xs:complexType name = "person">
    <xs:sequence>
        <xs:element name = "lastname" type="xs:string"/>
        <xs:element name = "age" type="xs:integer"/>
        <xs:element name = "dateborn" type="xs:date"/>
    </xs:sequence>
</xs:complexType>'''

#Many XML Schema Languages
#    Document Type Definition (DTD)
#    Standard Generalized Markup Language (ISO 8879:1986 SGML)
#    XML Schema from W3C - (XSD) ******************USING THIS ONE***********************

#W3C spec
#    We will focus on the World Wide Web Consortium (W3C) version
#    More commonly called XSD because its file names end in .xsd

#XSD Constraints
XsdConstraints = '''
<xs:element name="person">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="full_name" type="xs:string"
                minOccurs="1" maxOccurs="1"/>
            <xs:element name="child_name" type="xs:string"
                minOccurs="0" maxOccurs="10"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>'''
XmlDoc = '''
<person>
    <full_name>Tove Reefsnes</full_name>
    <child_name>Hege</child_name>
    <child_name>Stale</childe_name>
    <child_name>Jim</child_name>
    <child_name>Borge</child_name>
</person>'''

#XSD Data Types
'''
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>
'''
#Corresponding Inputs(Z corresponds to timezone)
'''
<customer>John Smith</customer>
<start>2002-09-24</start>
<startdate>2002-05-30T09:30:10Z</startdate>
<prize>999.50</prize>
<weeks>30</weeks>
'''

#JavaScipt Object Notation (JSON)*****************************
#    json.org
#    Not an international standard (RFCs)

#JSON example #1
import json
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data) #JSON represents data as nested "lists" and "dictionaries"
print(info) #{'name':'chuck', 'phone':{'type':'intl', 'number':'+1 734 303 4456'}, 'email': {'hide':'yes'}}
type(info) #<class 'dict'>
print('Name:', info["name"]) #Name: chuck
print('Hide:', info["email"]["hide"]) #Hide: yes

#JSON example #2
import json
input = '''[
    {
    "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {
    "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''
info = json.loads(input)
print(info) #[{'id':'001', 'x':'2', 'name':'Chuck'}, {'id':'009', 'x':'7', 'name':'Chuck'}]
type(info) #<class 'list'>
print('User count', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('#:',item['x'])

#Service Orientated Approach/Architecture
#    Most non-trivial web applications use services
#    They use services from other applications
#        Credit Card Charge
#        Hotel Reservation systems
#    Services publish the "rules" applications must follow to make use of the service (API)

#Multiple Systems
#    Initially - two systsems cooperate and split the problem
#    As the data/service becomes useful - multiple applications want to use the information/application

#Applicaion Program Interface
#    A contract for interaction
#    The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface.
#    THe software the provides the functionality described by an API is said to be an "implementation" of the API
#    An API is typically defined in terms of the programming language used to build an application
#    Similar to a contract, if you do this, then we're going to give you data this way; they set the rules up (url, xml, json)

import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
print(ctx) #<ssl.SSLContext object at 0x000001BF79BBC3B0>
type(ctx) #<class 'ssl.SSLContext'>
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print(ctx) #<ssl.SSLContext object at 0x000001BF79BBC3B0>
type(ctx) #<class 'ssl.SSLContext'>
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms) #'http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI' URL Encoded
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

#API Security and Rate Limiting
#    The compute resources to run these APIs are not "free"
#    The data provided by these APIs is usually valuable
#    The data providers might limit the number of requests per day, demand an API "key", or even charge for usage
#    They might change the rules as things progress...

#twitter2.py (Twurl+Urllib)
import urllib.request, urllib.parse, urllib.error
import twurl #in code3
import json
import ssl
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    #Retrive data using urllib
    urlhand = urllib.request.urlopen(url, context=ctx)
    data = urlhand.read().decode()
    js = json.loads(data)
    print(json.dumps(js, indent=2))
    headers = dict(urlhand.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])

#twitter3 (Tweepy)
import json
import ssl
import tweepy
# Twitter API keys and access tokens
consumer_key = 'rftwuJMKeILUTWbzeUtroU6Kb'
consumer_secret = 'TtLTQ6tiG7R78uKD5RyLBnqxEytjYZXAqYstzrhD7EKLUmBoMH'
access_token = '1532152275703046147-ndLZDkxsJIa9mCO5UXm84s0R0viBXb'
access_token_secret = 'coVCrPpPWQc1JAxWv2Bkuy8s6vEzlS73nEXsGSRXHjpYE'
# Create OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API instance
api = tweepy.API(auth)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    print('')
    acct = input('Enter Twitter Account:')
    if len(acct) < 1:
        break
    try:
        users = api.get_friends(screen_name=acct, count=5) #API request
        for user in users:
            print(user.screen_name)
            if not hasattr(user, 'status'):
                print('   * No status found')
                continue
            s = user.status.text
            print('  ', s[:50])
    except Exception as e:
        print('Error:', str(e))
print(api.rate_limit_status()['resources']['friends'])

#Chapter 14: Python Objects_____________________________________________________________________________________________________________________________________________________________________________________________________________

#This lecture is very much about defintions and mechanics for objects
#This lecture is a lot more about "how it works" and less about "how you use it"
#You won't get the bigger picture ultil this is all looked at in the context of a real problem
#So please suspend disbelief and learn technique for the next 50 or so slides..

#Object Oriented
#    A program is made up of many cooperating objects
#    Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects
#    A program is made up of one or more objects working together - objects make use of each other's capabilities

#Object
#    An Object is a bit of self-contained Code and Data
#    A key aspect of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
#    Objects have boundaries that allow us to ignore un-needed detail
#    We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...

#Definitions:
#    Class - a template - Dog
#    Method or Messsage - A defined capability of a class - bark(), learn()
#    Field or attribute - A bit of data in a class - length
#    Object or Instance - A particular instaance of a class - Lassie

#Terminology: Class
#    Defines the abstract characteristics of a thing (object), including the thing's characterisitics (its attributes, fields or properties) and the thing's behaviors (the things it can do, or methods, operations or features).
#    One might say that a class is a blueprint or factory that describes the nature of something.
#    For example, the class Dog would consist of traits shared by all dogs, such as breed and fur color (characterisitics), and the ability to bark and sit (behaviors)

#Terminology: Instance/Object
#    One can have an instance of a class or a particular object.
#    The instance is the actual object created at runtime.
#    In programmer jargon, the Lassie object is an instance of the Dog class.
#    The set of values of the attributes of a particular object is calleed its state.
#    The object consists of state and the behavior that's defined in the object's classs

#Terminology: Method
#    An object's abilites. In language, methods are verbs.
#    Lassie, being a Dog, has the ability to bark. So bark()is one of lassie's methods. She may have other methods as well, for example sit() or eat() or walk() or save_timmy().
#    Within the program, using a method usually affects only one particular object; all Dogs can bark, but you need only one particular dog to do the barking
#   Mthod and Message are often used interchangably

#class example
class PartyAnimal:
    x = 0 #default attribute
    def party(self): #This is a method, not a function, because it lives inside of a class
        self.x = self.x +1
        print("So far", self.x)
an = PartyAnimal()
an.party() #equivalent to PartyAnimal.party(an)
PartyAnimal.party(an)
an.party()
an.party()

#We can use dir() to find the "capabilities" of our newly created class

#Object Lifecyle
#    Objects are created, used and discarded
#    We have special blocks of code (methods) that get called
#        At the momment of creation (constructor) (used a lot)
#        At the moment of destruction (destructor) (seldom used)

#Constructor
#    The primary purpose of the constructor is to set up some instance variables to have the proper inital values when the object is created
#    In Object Oriented Programming (OOP), a constructor in a class is a special block of statements called when an object is called
class PartyAnimal:
    x = 0
    def __init__(self): #prints when an = PartyAnimal()
        print('I am constructed')
    def party(self):
        self.x = self.x +1
    def __del__(self): #prints when an = 42
        print('I am destructed', self.x)

#Many instances
#    We can create lots of objects - the class is the template for the object
#    We can store each distinct object in its own variable
#    We call this having multiple instances of the same class
#    Each instance has its own copy of the instance variables

#Constructors can have additional parameters.
#    These can be used to set up the instance variables for the particular instance of the class(i.e., for the particular object)
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z): #self has to be first #z becomes the input for s = PartyAnimal("Sally")
        self.name = z
        print(self.name, "contructed")
    def party(self):
        self.x = self.x + 1
        party(self.name, "party count", self.x)
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()

#Inheritance
#    When we make a new class - we can reuse an existing class and inherit all the capabilites of an existing class and then add our little bit to make our new class
#    Another form of store and reuse
#    Write once - reuse many times
#    The new class (child) has all the capabilites of the old class (parent) - and then some more

#Terminology: Inheritance
#    'Subclasses' are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own

#FootballFan is a class which extends Party Animal. It has all the capabilties of PartyAnimal and more.
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
class FootballFan(PartyAnimal): #Inherits everything that is PartyAnimal to FootballFan objects #There is also not __init__() here, so PartyAnimal init is used.
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points:", self.points)

#Definitions
#    Class - a template
#    Attribute - A variable whithin a class
#    Method - A function within a class
#    Object - A particular instance of a class
#    Constructor - Code that runs when an object is created
#    Inheritance - The ability to extend a class to make a new class

#Summary
#    OOP is a very structured approach to code reuse
#    We can group data and functionality together and create many independent instances of a class

#Chapter 15: Relational Databases and SQLite____________________________________________________________________________________________________________________________________________________________________________________________________________________

#Random Access
#    When you can randomly access data...
#    How can you layout data to be most efficient?
#    Sorting might not be the best idea

#Relational Databases
#    Rational databases model data by storing rows and columns in tables
#    The power of relational databases:
#        Ability to retrieve data from those tables and in particular where there are multiple tables and the relationships between those tables involved in the query.

#Terminology
#    Database - contains many tables
#    Relation (or table) - a set of tuples that have the same overall attributes
#    Tuple (or row) - a set of fields that generally represents an "object" and information about that object
#    Objects - typically physical objects or concepts
#    Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row

#SQL (Structured Query Language)
#    (C)reate a table
#    (R)etrieve some data
#    (U)pdate data
#    (D)elete data

#Web Applications w/ Databases
#    Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
#    Database Administrator - Monitors and adjusts the database as the program runs in production
#    Often both people participating in the building of the "Data model"

#Database Administrator:
#    A database administrator (DBA) is a person responsible for the design, implementation, maintenance, and repair of an organization's database
#    The role includes the development and design of database strategies, monitoring, and improving database performance and capacity, and planning for future expansion requirements.
#    They may also plan, coordinate, and implement security measures to safeguard the database.

#Database Model
#    A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system.
#    In other words, a "database model" is the application of a data model when used in conjuction with a database management systemm.

#Common Database Systems
#    Three major Database Management Systems in wide use:
#        Oracle - Large, commercial, enterprise-scale, very very tweakable
#        MySql - Simpler but very fast and scalable - commerical open source
#        SqlServer - Very nice - from Microsoft (also Access)
#    Many other smaller projects, free and open source
#        HSQL, SQLite, Postgres,...

#Python for Everybody Database Handout
#    https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt
Single Table SQL #every reserved word and non-text can be lower case or uppercase, doesn't matter

CREATE TABLE "Users" ("name" TEXT, "email" TEXT);

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu'); #Inserts a row into the table
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu'); #Need to add ';' when executing multiple lines of code in SQL
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');

DELETE FROM Users WHERE email='ted@umich.edu' #Deletes a row in a table based on a selection criteria
UPDATE Users SET name="Charles" WHERE email='csev@umich.edu' #Allows the updating of a field with a where clause
SELECT * FROM Users #'*' means 'ALL'
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY email #You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
SELECT * FROM Users ORDER BY name DESC #descending order; if the 'desc' is after users, then no change and prints out ascending order; this means that the 'desc' operates on the object directly before.

#emaildb.py
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')
fh = open('mbox-short.txt')
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    lst = cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))  #the "?" prevents SQL injection (cybersecurity vulnerabilty); the email in the tuple replaces the "?"; the comma is there to make it a tuple
#for every cur.execute(), there will be a location value outputed into console; lst = cur.execute() prevents that.
    row = lst.fetchone() #row is tuple of the first one in the table; removes tuple from the selected set, but leaves database untouched
    if row is None:
        op = cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,)) #str and tuple must be included
    else:
        op = cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit() #saves to hard drive; allows sqlite to update with new information
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1]) #row is a tuple
cur.close()

#twspider.py
from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)
    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()
cur.close()

#Database Design
#    Database design is an art form of its own with particular skills and experience
#    Our goal is to avoid the really bad mistakes and design clean and easily understood databases
#    Others may performance tune things later
#    Database design starts with a picture

#Building a Data Model
#    Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationships
#    Basic Rule: Don't put the same string data in twice: use a relationship instead #everyhing else points to that string data
#    When there is one thing in the "real world" there should be one copy of that thing in the database

#For each "piece of info"...
#    Is the column an object or an attribute of another object?
#    Once we define objects, we need to define the relationships between objects.

#Representing Relationships in a Database
#Database Normalization (3NF- Third Normal Form)
#    There is "tons" of database theory - way too much to understand without excessive predicate calculus
#    Do not replicate data - reference data - point at data
#    Use integers for keys and for references
#    Add a special "key" column to each table which we will make references to.
#        By convention, many programmers call this column "id"

#Integer Reference Pattern
#    We use integers to reference rows in another table
#       Artist {id:name}: {1:'Led Zepplin', 2:'AC/DC'}
#       Album {id:artist_id:title}: {1:2:'Who Made Who', 2:1:'IV'}
#       artist_id points to id in artist table

#Three Kinds of Keys
#    Primary key (id) - generally an integer auto-increment field
#    Logical key (title) - What the outside world useses for lookup
#    Foreign key (artist_id) - generally an integer key pointing to a row in another table

#Key Rules
#    Best practices:
#        Never use your logical key as the primary key; always make the primary key (id) an integer
#        Logical keys can and do change, albeit slowly
#        Relationships that are based on matching string fields are less efficient than integers

#Foreign Keys
#    A foreign key is when a table has a column that contains a key which points to the primary key of another table
#    When all primary keys are integers, then all foreign keys are integers - this is good - very good

#Relationship Building (in tables)
#    "Belongs to" is like an arrow pointing from the foreign key of one table to the primary key of another table
#    ex. song (logical key of title table) belongs to a certain album (logical key of album table)

#Multi-Table SQL:
CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT);
CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    artist_id INTEGER,
    "title" TEXT);
CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT);
CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER,
    "title" TEXT, "count" INTEGER);

INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;

#Relational Power
#    By removing the replicated data and replacing it with references to a single sopy of each bit of data:
#        We can build a "web" of information that the relational database can read through very quickly - even for very large amounts of data
#    Often when you want some data it comes from a number of tables linked by these foreign keys

#The JOIN Operation
#    The JOIN operation links across several tables as part of a select operation
#    You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause

SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
#'Album.title, Artist.name' is what we want to see; 'Album'/'Artist' are the tables that hold the data. 'Album.artist_id = Artist.id' is how the tables are linked
#Order of columns selected is based on "Album.title, Artist.name" part.
#"Album JOIN Artist" = "Artist JOIN Album"

SELECT Album.title, Album.artist_id, Artist.id, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
#Basically the connection between distinct tables, and gluing/merging rows from different tables together based on a certain criteria using an ON clause
#The ON clause matches columns based on a criteria; The linkage "Track.genre_id = Genre.id" is the glue between correponding rows in Genre and Track tables.

SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre
#Joining two tables without an ON clause gives all possible combination of rows
#    Total num rows = (Table 1 # rows) * (Table 2 # rows)
#The ON clause filters the overall JOIN table through a certain criteria, such as Track.genre_id = Genre.id
#In other words, the overall JOIN operation is followed through, then filtered by the ON clause.

SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id
#This forms the final table that we've been trying to contruct since the beginning

#tracks.py
import xml.etree.ElementTree as ET
import sqlite3
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id  INTEGER, title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT  UNIQUE, album_id  INTEGER, len INTEGER, rating INTEGER, count INTEGER);
''')
#Order: Type, Nullity, Key, Autoincrement, Uniqueness
fname = 'Library.xml'
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
#the input d is a ElementTree object
    found = False
    for child in d:
        #for all the subsections exclusively one below Element Tree 'd'
        if found:
            return child.text #returns child.text and breaks out of loop
        if child.tag == 'key' and child.text == key:
            found = True
    return None
stuff = ET.parse(fname) #simlar to ET.fromstring(); ET.parse() parses XML from a file, instead of from a string
tracks = stuff.findall('dict/dict/dict') #finds all <dict> along the third level
print('Dict count:', len(tracks)) #404
for track in tracks:
    if ( lookup(track, 'Track ID') is None ) : continue
    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')
    if name is None or artist is None or album is None : continue
    print(name, artist, album, count, rating, length)
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', ( artist, ) )
    #'INSERT OR IGNORE' means to ignore value if it's already there (the constraint set when creating the table was uniqueness)
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute('INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES ( ?, ?, ?, ?, ? )', ( name, album_id, length, rating, count ) )
    conn.commit()
cur.execute('SELECT Track.title, Album.title, Artist.name FROM Track JOIN Album JOIN Artist ON Track.album_id = Album.id AND Album.artist_id = Artist.id')

#Many to Many
#    Sometimes we need to model a relationship that is many-to-many
#    We need to add a "connection"/junction table with two foreign keys
#    There is usually no seperate primary key for the junction table
#    You would create a middle table that would simulate a many-to-many relationshp to two many-to-one relationships
#    A member from the connector/junction table has a unique combination of the foreign keys of the tables that have a many-to-many relationship with each other.
#    Almost like the tic-tac-toe board or the punnett square when assessing the distinct combinations of the many-to-many relationship members


Many-Many Relationship

CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE, email TEXT);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id));
#the role of the member is modeled at the connection; where the member is being generated
#The primary key here ensures that the foreign key combination is unique
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
  FROM User JOIN Member JOIN Course
  ON Member.user_id = User.id AND Member.course_id = Course.id
  ORDER BY Course.title, Member.role DESC, User.name

#Complexity Enables Speed
#    Complexity makes speed possible and allows you to get very fast results as the data size grows
#    By normalizing the data and linking it with integer keys:
#        the overall amount of data which the relational database must scan is far lower than if the data were simply flattened out
#    it might seem like a tradeoff:
#        spend some time designing your database so it continues to be fast when your application is a success

#Additional SQL Topics
#    Indexes improve performance for things like string fields
#    Constraints on data - (cannot be NULL, etc.)
#    Transactions - allow SQL operations to be grouped and done as a unit

#Summary
#    Relational databases allow us to scale to very large amounts of data
#    The key is to have one copy of any data element and use relations and joins to link the data to multiple places
#    This greatly reduces the amount of data which must be scanned when doing complex operations across large amounts of data
#    Database and SQL design is a bit of an art form

#roster.py
import json
import sqlite3
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()
# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id))
''')#The primary key here ensures that the foreign key combination is unique
fname = 'roster_data_sample.json'
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],
str_data = open(fname).read()
json_data = json.loads(str_data)
for entry in json_data:
    name = entry[0]
    title = entry[1]
    print((name, title))
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( ?, ? )', ( user_id, course_id ) )
    conn.commit()

#twfriends.py
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, ))
            conn.commit()
            if cur.rowcount != 1: #rowcount returns the number of rows affected by the last executed sqlite statement
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid #lastrowid returns the the ID/Primary Key of the last INSERTED row
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err: #Doesn't blow up in the old fashion; It outputs what went wrong with Try
        print('Failed to Retrieve', err)
        break
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break
    # Debugging
    # print(json.dumps(js, indent=4))
    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue
    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))
    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()

#Chapter 16: Data Visualization____________________________________________________________________________________________________________________________________________________________________________________________________________________

#Multi-Step Data Analysis
#    Data Source (API,HTML,etc) -> Gather (Slow and Restartable Process) -> Raw Database (Large in size) -> Clean/Processed Database (Small in size) -> Visualization or Analyze

#Many Data Mining Technologies
#    https://hadoop.apache.org/
#    http://spark.apache.org/
#    https://aws.amazon.com/redshift/
#    http://community.pentaho.com/

#"Personal Data Mining"
#    Our goal is to make you better programmers - not to make you into data mining experts

#GeoData
#    Makes a Google Map from user entered data
#    Uses the Google Geodata API
#    Caches data in a database to avoid rate limiting and allow restarting
#    Visualized in a browser using the Google Maps API

#geoload.py
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), )) #memoryview refers to the address value itself and does not create a copy
    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    try:
        js = json.loads(data) #converts the json string into a corresponding dictionary
    except:
        print(data)  # We print in case unicode causes an error
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

#geodump.py
import sqlite3
import json
import codecs
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue
    if not('status' in js and js['status'] == 'OK') : continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "") #Replaces all (') with (); Removes (') from string
    try :
        print(where, lat, lng)
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "[" + str(lat) + "," + str(lng) + ", '" + where + "']"
        fhand.write(output)
    except:
        continue
fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

#Page Rank
#    Write a simple web page crawler
#    Compute a simple version of Google's Page Rank algorithm
#    Visualize the resulting network

#Search Engine Architecture
#    Web Crawling
#    Index Building
#    Searching

#Web Crawler
#    A Web crawler is a computer program that browses the World Wide Web in a methodical, automated manner.
#    Web crawlers are mainly used to create a copy of all the visited pages for later processing by a search engine that will index the downloaded pages to provide fast searches.

#Web Crawler
#    Retrieve a page
#    Looks through the page for links
#    Adds the links to a list of "to be retrieved" sites
#    Repeat...

#Web Crawling Policy
#    A selection policy that states which pages to download
#    A re-visit policy that states when to check for changes to the pages
#    A politenss policy that states how to avoid overloading Web sites
#    A paralleliation policy that states how to coordinate distributed Web crawlers

#robots.txt
#    A way for a web site to communicate with web crawlers
#    An informal and voluntary standard
#    Sometimes folks make a "Spider Trap" to catch "bad" spiders

#Search Indexing
#    Search engine indexing collects, parses, and stores data to facilitate fast and accurate information retrieval.
#    The purpose of storing an index is to optimize speed and performance in finding relevant documents for a search query.
#    Without an index, the search engine would scan every document in the corpus, which would require considerable time and computing power

#spider.py
import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.executescript('''CREATE TABLE IF NOT EXISTS Pages (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT, error INTEGER, old_rank REAL, new_rank REAL);
    CREATE TABLE IF NOT EXISTS Links (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id));
    CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE);
    ''')
#Pages is the table with vertices; Links creates the connections between each vertex; Web is the table with website input
# Check to see if we are already in progress...
cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1') # html is NULL means that it hasn't been retrieved yet; retrives what hasn't been retrieved yet from the Pages table
#This SELECT is used for detecting if there any unretrieved pages
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl. Remove spider.sqlite to start a fresh crawl.")
else :
    starturl = input('Enter web url or enter: ')
    if ( len(starturl) < 1 ) : starturl = 'https://www.dr-chuck.com/'
    if ( starturl.endswith('/') ) : starturl = starturl[:-1] #removes (/) from starturl
    web = starturl
    if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
        pos = starturl.rfind('/') #finds last occurance of (/)
        web = starturl[:pos] #splices and takes starturl up until the last (/) exclusively.
    if ( len(web) > 1 ) :
        cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) ) #web consists of the website inputs
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) ) #Pages involves all the urls, including the input url, retrieved; Partially forms the url for the rest
        conn.commit()
# Get the current webs
cur.execute('''SELECT url FROM Webs''') #selects all the code that needs to be retrieved from (the starting urls)
#This part restarts the items selected
webs = list()
for row in cur:
    webs.append(str(row[0]))
print(webs)
many = 0
while True:
    if ( many < 1 ) :
        sval = input('How many pages:') #how many iterations of this While loop
        if ( len(sval) < 1 ) : break
        many = int(sval)
    many = many - 1 #after each iteration, "many" decreases by one
    cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1') #fromid and url name from unretrieved links (has to be here because the last time wasn't saved)
    #Also because of the While loop, this part has to be included in here
    try:
        row = cur.fetchone()
        # print row
        fromid = row[0]
        url = row[1]
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break
    print(fromid, url, end=' ')
    # If we are retrieving this page, there should be no links from it
    cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) ) # restarts the links connections from the starting url
    try:
        document = urlopen(url, context=ctx)
        html = document.read() #reads the retrieved page
        if document.getcode() != 200 : #getcode() retrieves HTTP status code; 200 = 'OK'
            print("Error on page: ",document.getcode())
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )
        if 'text/html' != document.info().get_content_type() : #outputs the type of website (txt/html, jpg, htm)
            print("Ignore non text/html page")
            cur.execute('DELETE FROM Pages WHERE url=?', ( url, ) ) #removes url from possible nodes
            conn.commit()
            continue
        print('('+str(len(html))+')', end=' ') #the (+) within the string allows for input of variables into strings without concatenation (str + str + str)
        soup = BeautifulSoup(html, "html.parser")
    except KeyboardInterrupt: #The usage of ^C in the command prompt would break it out of loop
        print('')
        print('Program interrupted by user...')
        break
    except:
        print("Unable to retrieve or parse page")
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        conn.commit()
        continue
    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url ) )
    conn.commit()
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if ( href is None ) : continue
        # Resolve relative references like href="/contact"
        up = urlparse(href) #breaks url into pieces
        if ( len(up.scheme) < 1 ) : #the scheme is either http or https if non-empty
            href = urljoin(url, href)
        ipos = href.find('#')
        if ( ipos > 1 ) : href = href[:ipos]
        if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue #filters non-text pages (such as json or XML)
        if ( href.endswith('/') ) : href = href[:-1]
        # print href
        if ( len(href) < 1 ) : continue
		# Check if the URL is in any of the webs
        found = False
        for web in webs:
            if ( href.startswith(web) ) :
                found = True
                break #breaks out of For loop
        if not found : continue #filters out pages that don't come directly from the input web
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) ) #insertion of new url
        count = count + 1
        conn.commit()
        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, )) #toid is the id of the newly inserted url
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        # print fromid, toid
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )
    print(count)
cur.close()

#sprank.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
# Find the ids that send out page rank - we only are interested
# in pages in the SCC that have in and out links
cur.execute('''SELECT DISTINCT from_id FROM Links''') #Finds all distinct from_id
from_ids = list()
for row in cur:
    from_ids.append(row[0]) #Inserts all possible (from_id)'s in the db into from_ids list
# Find the ids that receive page rank
to_ids = list()
links = list()
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''') #Finds distinct combinations of from_id and to_id
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id : continue #links to itself
    if from_id not in from_ids : continue #from_id is not a from_id somehow
    if to_id not in from_ids : continue #to_id page doesn't led to another page
    links.append(row) #links is a list of tuples (from_id, to_id)
    if to_id not in to_ids : to_ids.append(to_id) #inserts certain to_id into to_id list, such that the page leads to another page (to_id is in to_ids)
# Get latest page ranks for strongly connected component
prev_ranks = dict() # nodeid : prev_rank
for nodeid in from_ids:
    cur.execute('''SELECT new_rank FROM Pages WHERE id = ?''', (nodeid, ))
    row = cur.fetchone()
    prev_ranks[nodeid] = row[0] #old rank is being set to the rank the page was before (newrank)
sval = input('How many iterations:')
many = 1
if ( len(sval) > 0 ) : many = int(sval)
# Sanity check
if len(prev_ranks) < 1 : #there are no previous ranks, and therefore no pages in Pages table
    print("Nothing to page rank.  Check data.")
    quit()
# Lets do Page Rank in memory so it is really fast
for i in range(many): #iterates as "many" times; range(many) is [0,1,2,..., many - 1]
    # print prev_ranks.items()[:5]
    next_ranks = dict();
    total = 0.0 #overall total sum of all old ranks
    for (nodeid, old_rank) in list(prev_ranks.items()):
        total = total + old_rank
        next_ranks[nodeid] = 0.0 # nodeid : 0.0
    # print total
    # Find the number of outbound links and sent the page rank down each
    for (nodeid, old_rank) in list(prev_ranks.items()): #list(prev_ranks.items) is (nodeid, old_rank)
        give_ids = list()
        for (from_id, to_id) in links:
            if from_id != nodeid : continue #if the given node is not also the given node_id, then restart loop
           #  print '   ',from_id,to_id
            if to_id not in to_ids: continue
            give_ids.append(to_id) #all corresponding to_id's w.r.t. nodeid = from_id are placed into give_ids
        #this loop basically gathers all to_id's from a nodeid, and places them into give_ids
        if ( len(give_ids) < 1 ) : continue #if no branching pages, then skip node
        amount = old_rank / len(give_ids) #if more branching pages from node then amount decreases; less of node is distributed among branches
        # print node, old_rank,amount, give_ids
        for toid in give_ids:
            next_ranks[toid] = next_ranks[toid] + amount #the node rank is equally distrubuted to each branching page's new rank
    newtot = 0 #overall total sum of all current given ranks
    for (nodeid, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    evap = (total - newtot) / len(next_ranks)
    # print newtot, evap
    for nodeid in next_ranks:
        next_ranks[nodeid] = next_ranks[nodeid] + evap #calculates remaining values and distributes it evenly among every single node
    newtot = 0 #overall total sum of ranks after adjustment; should be equal to "total" now
    for (nodeid, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank
    # Compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0 #added up absolute difference between new and old ranks
    for (nodeid, old_rank) in list(prev_ranks.items()):
        new_rank = next_ranks[nodeid]
        diff = abs(old_rank-new_rank)
        totdiff = totdiff + diff
    avediff = totdiff / len(prev_ranks) #average difference
    print(i+1, avediff)
    # rotate
    prev_ranks = next_ranks
# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('''UPDATE Pages SET old_rank=new_rank''')
for (id, new_rank) in list(next_ranks.items()) :
    cur.execute('''UPDATE Pages SET new_rank=? WHERE id=?''', (new_rank, id))
conn.commit()
cur.close()

#spreset.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
conn.commit()
cur.close()
print("All pages set to a rank of 1.0")

#spdump.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')
count = 0
for row in cur :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
cur.close()

#spjson.py
import sqlite3
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
print("Creating JSON output on spider.js...")
howmany = int(input("How many nodes? "))
cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
    FROM Pages JOIN Links ON Pages.id = Links.to_id
    WHERE html IS NOT NULL AND ERROR IS NULL
    GROUP BY id ORDER BY id,inbound''') # 'COUNT(from_id)' is represented as 'inbound'; 'GROUP BY id' means that each result is done seperately by Pages.id
    #With respect to each pages.id, count(from_id) is performed as if each pages.id is a seperate table
fhand = open('spider.js','w') #completely deletes all information on spider.js and starts anew
nodes = list()
maxrank = None
minrank = None
for row in cur : #this loop finds the minrank and maxrank
    nodes.append(row)
    rank = row[2]
    if maxrank is None or maxrank < rank: maxrank = rank
    if minrank is None or minrank > rank : minrank = rank
    if len(nodes) > howmany : break #only first 'howmany' nodes are considered (ordered by id,inbound)
if maxrank == minrank or maxrank is None or minrank is None:
    print("Error - please run sprank.py to compute page rank")
    quit()
fhand.write('spiderJson = {"nodes":[\n') #begins nodes section
count = 0
map = dict() # id : count(autoincrement)
ranks = dict() # id : rank
for row in nodes : #(inbound, old_rank, new_rank, id, url)
    if count > 0 : fhand.write(',\n') #starts a new line after each entry
    rank = row[2] #new_rank
    rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) #scales rank based on minrank and maxrank: ranges from 0 to 19
    fhand.write('{' + '"weight":' + str(row[0]) + ',"rank":' + str(rank) + ',') #"weight" = inbound, "rank" = rank
    fhand.write(' "id":' + str(row[3]) + ', "url":"' + row[4] + '"}') #"id" = id, "url" = url
    map[row[3]] = count
    ranks[row[3]] = rank
    count = count + 1
fhand.write('],\n') #ends the nodes section of the json doc
cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
fhand.write('"links":[\n') #begins links section
count = 0
for row in cur : #(from_id, to_id)
    # print row
    if row[0] not in map or row[1] not in map : continue #only considers links part of nodes
    if count > 0 : fhand.write(',\n') #stars new line after each entry
    rank = ranks[row[0]] #from_id's rank
    fhand.write('{"source":' + str(map[row[0]]) + ',"target":' + str(map[row[1]]) + ',"value":3}')
    count = count + 1
fhand.write(']};') #ends file
fhand.close()
cur.close()
print("Open force.html in a browser to view the visualization")

#Mailing Lists - Gmane
#    Crawl the archive of a mailing list
#    Do some analysis / cleanup
#    Visualize the data as world cloud and lines

#Warning: This Dataset is more than 1GB
#    Don't point this application at gmane.org
#    use http://mbox.dr-chuck.net/sakai.devel/4/5 instead

#gmane.py
import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
# Not all systems have this so conditionally define parser
try:
    import dateutil.parser as parser
except:
    pass
def parsemaildate(md) :
    # See if we have dateutil
    try:
        pdate = parser.parse(tdate) #dateutil.parser
        test_at = pdate.isoformat() #datetime
        return test_at
    except:
        pass
    # Non-dateutil version - we try our best
    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()
    # Try a bunch of format variations - strptime() is *lame*
    dnotz = None
    for form in [ '%d %b %Y %H:%M:%S', '%d %b %Y %H:%M:%S',
        '%d %b %Y %H:%M', '%d %b %Y %H:%M', '%d %b %y %H:%M:%S',
        '%d %b %y %H:%M:%S', '%d %b %y %H:%M', '%d %b %y %H:%M' ] :
        try:
            dnotz = datetime.strptime(notz, form) #datetime
            break
        except:
            continue
    if dnotz is None :
        # print 'Bad Date:',md
        return None
    iso = dnotz.isoformat()
    tz = "+0000"
    try:
        tz = pieces[4]
        ival = int(tz) # Only want numeric timezone values
        if tz == '-0000' : tz = '+0000'
        tzh = tz[:3]
        tzm = tz[3:]
        tz = tzh+":"+tzm
    except:
        pass
    return iso+tz
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()
baseurl = "http://mbox.dr-chuck.net/sakai.devel/"
cur.execute('''CREATE TABLE IF NOT EXISTS Messages
    (id INTEGER UNIQUE, email TEXT, sent_at TEXT,
     subject TEXT, headers TEXT, body TEXT)''')
# Messages (id, email, sent_at, subject, headers, body)
# Pick up where we left off
start = None
cur.execute('SELECT max(id) FROM Messages' ) #selects latest id
try:
    row = cur.fetchone()
    if row is None :
        start = 0
    else:
        start = row[0] #picking up where we left off
except:
    start = 0 #one less than id to retrieve
if start is None : start = 0
many = 0 #number of messages to recieve
count = 0 #number of messages recieved
fail = 0 #number of failed emails
while True: #done per email
    if ( many < 1 ) :
        conn.commit()
        sval = input('How many messages:')
        if ( len(sval) < 1 ) : break
        many = int(sval)
    start = start + 1
    cur.execute('SELECT id FROM Messages WHERE id=?', (start,) )
    try:
        row = cur.fetchone()
        if row is not None : continue #if already inserted, then continue to next email
    except:
        row = None
    many = many - 1
    url = baseurl + str(start) + '/' + str(start + 1)
    text = "None"
    try:
        # Open with a timeout of 30 seconds
        document = urllib.request.urlopen(url, None, 30, context=ctx)
        text = document.read().decode()
        if document.getcode() != 200 :
            print("Error code=",document.getcode(), url)
            break
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except Exception as e:
        print("Unable to retrieve or parse page",url)
        print("Error",e)
        fail = fail + 1
        if fail > 5 : break #allows 5 fails for distinct emails
        continue
    print(url,len(text))
    count = count + 1 #one more email is successfully retrieved
    if not text.startswith("From "):
        print(text)
        print("Did not find From ")
        fail = fail + 1
        if fail > 5 : break
        continue
    pos = text.find("\n\n")
    if pos > 0 : #position of where "\n\n" first starts
        hdr = text[:pos] #header
        body = text[pos+2:] #body
    else:
        print(text)
        print("Could not find break between headers and body")
        fail = fail + 1
        if fail > 5 : break
        continue
    email = None
    x = re.findall('\nFrom: .* <(\S+@\S+)>\n', hdr) #creates a list of all instances
    if len(x) == 1 : #found a single email
        email = x[0];
        email = email.strip().lower()
        email = email.replace("<","")
    else:
        x = re.findall('\nFrom: (\S+@\S+)\n', hdr)
        if len(x) == 1 :
            email = x[0];
            email = email.strip().lower()
            email = email.replace("<","")
    date = None
    y = re.findall('\Date: .*, (.*)\n', hdr)
    if len(y) == 1 :
        tdate = y[0]
        tdate = tdate[:26]
        try:
            sent_at = parsemaildate(tdate) #converts original date into another format form
        except:
            print(text)
            print("Parse fail",tdate)
            fail = fail + 1
            if fail > 5 : break
            continue
    subject = None
    z = re.findall('\Subject: (.*)\n', hdr)
    if len(z) == 1 : subject = z[0].strip().lower();
    # Reset the fail counter
    fail = 0
    print("   ",email,sent_at,subject)
    cur.execute('''INSERT OR IGNORE INTO Messages (id, email, sent_at, subject, headers, body)
        VALUES ( ?, ?, ?, ?, ?, ? )''', ( start, email, sent_at, subject, hdr, body))
    if count % 50 == 0 : conn.commit()
    if count % 100 == 0 : time.sleep(1)
conn.commit()
cur.close()

#gmodel.py
import sqlite3
import time
import re
import zlib #used for compressing data
from datetime import datetime, timedelta
# Not all systems have this
try:
    import dateutil.parser as parser
except:
    pass
dnsmapping = dict()
mapping = dict()
#fixsender('s.swinsburg@lancaster.ac.uk')
def fixsender(sender,allsenders=None) :
    global dnsmapping #these are global variables, which can be assessed and modified within the function; these variables are assumed to be defined outside of the function
    global mapping
    if sender is None : return None
    sender = sender.strip().lower() #s.swinsburg@lancaster.ac.uk; steve.swinsburg@swinsborg.com
    sender = sender.replace('<','').replace('>','') #s.swinsburg@lancaster.ac.uk; steve.swinsburg@swinsborg.com
    # Check if we have a hacked gmane.org from address
    if allsenders is not None and sender.endswith('gmane.org') :
        pieces = sender.split('-')
        realsender = None
        for s in allsenders:
            if s.startswith(pieces[0]) :
                realsender = sender
                sender = s
                # print(realsender, sender)
                break
        if realsender is None :
            for s in mapping:
                if s.startswith(pieces[0]) :
                    realsender = sender
                    sender = mapping[s]
                    # print(realsender, sender)
                    break
        if realsender is None : sender = pieces[0]
    mpieces = sender.split("@") #[s.swinsburg, lancaster.ac.uk]; [steve.swinsburg, swinsborg.com]
    if len(mpieces) != 2 : return sender #checks if only one email was aquired
    dns = mpieces[1] #lancaster.ac.uk; swinsborg.com
    x = dns
    pieces = dns.split(".") #[lancaster, ac, uk]; [swinsborg, com]
    if dns.endswith(".edu") or dns.endswith(".com") or dns.endswith(".org") or dns.endswith(".net") :
        dns = ".".join(pieces[-2:]) #join last two items in list with '.'; 'swinsborg.com'
    else:
        dns = ".".join(pieces[-3:]) #join last three items in list with '.'; 'lancaster.ac.uk'
    # if dns != x : print(x,dns)
    # if dns != dnsmapping.get(dns,dns) : print(dns,dnsmapping.get(dns,dns))
    dns = dnsmapping.get(dns,dns) #attempts to retrive value with key 'dns' (in case if dns changed emails), otherwise returns dns
    return mpieces[0] + '@' + dns #s.swinsburg@lancaster.ac.uk; steve.swinsburg.swinsborg.com
#parsemaildate('8 Dec 2005 23:34:30 -0600')
def parsemaildate(md) :
    # See if we have dateutil; otherwise using methods from datetime.datetime
    try:
        pdate = parser.parse(md) #dateutil.parser #datetime.datetime(2005,12,8,34,30, tzinfo=tzoffset(None, -21600))
        test_at = pdate.isoformat() #'2005-12-08T23:34:30-06:00'
        return test_at
    except:
        pass
    # Non-dateutil version - we try our best
    pieces = md.split() #['8','Dec','2005','23:34:30','-0600']
    notz = " ".join(pieces[:4]).strip() #'8 Dec 2005 23:34:30'
    # Try a bunch of format variations - strptime() is *lame*
    dnotz = None
    for form in [ '%d %b %Y %H:%M:%S', '%d %b %Y %H:%M:%S',
        '%d %b %Y %H:%M', '%d %b %Y %H:%M', '%d %b %y %H:%M:%S',
        '%d %b %y %H:%M:%S', '%d %b %y %H:%M', '%d %b %y %H:%M' ] :
        #lowercase means abbrivated for %b, and %y
        try:
            dnotz = datetime.strptime(notz, form) #dnotz = datetime.datetime(2005,12,8,23,34,30); form = '%d %b %Y %H:%M:%S'
            break
        except:
            continue
    if dnotz is None :
        # print('Bad Date:',md)
        return None
    iso = dnotz.isoformat() #'2005-12-08T23:34:30'
    tz = "+0000"
    try:
        tz = pieces[4] '-0600'
        ival = int(tz) # Only want numeric timezone values; -600
        if tz == '-0000' : tz = '+0000'
        tzh = tz[:3] #'-06'
        tzm = tz[3:] #'00'
        tz = tzh + ":" + tzm #'-06:00'
    except:
        pass
    return iso+tz #'2005-12-08T23:34:30-06:00'
# Parse out the info...
#parseheader(headers, allsenders)
hdr = '''From news@gmane.org Tue Mar 04 03:33:20 2003
From: "Glenn R. Golden" <ggolden@umich.edu>
Subject: call for participation: developers documentation
Date: Thu, 8 Dec 2005 23:34:30 -0600
Lines: 28
Message-ID: <B7EAF76E-3366-4AE3-BDD6-6743707FEBA9@umich.edu>
Mime-Version: 1.0
Content-Type: text/plain; charset=US-ASCII; delsp=yes; format=flowed
Content-Transfer-Encoding: 7bit
X-From: postmaster@collab.sakaiproject.org Fri Dec 09 06:38:09 2005
Return-path: <postmaster@collab.sakaiproject.org>
Received: from bonecollector.mr.itd.umich.edu ([141.211.93.140])
	by ciao.gmane.org with esmtp (Exim 4.43)
	id 1EkawZ-0002jO-37
	for gccsd-sakai-dev@m.gmane.org; Fri, 09 Dec 2005 06:37:19 +0100
Received: FROM sharkfin.ds.itd.umich.edu (sharkfin.ds.itd.umich.edu [141.211.253.161])
	BY bonecollector.mr.itd.umich.edu ID 4399180C.A1939.12235 ;
	 9 Dec 2005 00:37:16 -0500
Received: from sharkfin.ds.itd.umich.edu ([127.0.0.1])
          by sharkfin.ds.itd.umich.edu (JAMES SMTP Server 2.1.3) with SMTP ID 423
          for <sakai-dev@collab.sakaiproject.org>;
          Fri, 9 Dec 2005 00:34:25 -0500 (EST)
Received: from relay1.mail.twtelecom.net (ns-map.ds.itd.umich.edu [141.211.253.192])
	by sharkfin.ds.itd.umich.edu (Postfix) with ESMTP id A4AB01C02F
	for <sakai-dev@collab.sakaiproject.org>; Fri,  9 Dec 2005 00:34:25 -0500 (EST)
Received: from [172.29.173.27] (unknown [66.194.95.2])
	by relay1.mail.twtelecom.net (Postfix) with ESMTP id AE54C5037
	for <sakai-dev@collab.sakaiproject.org>; Thu,  8 Dec 2005 23:29:25 -0600 (CST)
X-Content-Type-Outer-Envelope: text/plain; charset=US-ASCII; delsp=yes; format=flowed
To: sakai-dev <sakai-dev@collab.sakaiproject.org>
X-Mailer: Apple Mail (2.746.2)
X-Content-Type-Message-Body: text/plain; charset=US-ASCII; delsp=yes; format=flowed'''
#allsenders is a list with all senders in it, excluding those with gmane.org
def parseheader(hdr, allsenders=None):
    if hdr is None or len(hdr) < 1 : return None
    sender = None
    x = re.findall('\nFrom: .* <(\S+@\S+)>\n', hdr) #['ggolden@umich.edu']
    if len(x) >= 1 :
        sender = x[0] #'ggolden@umich.edu'
    else:
        x = re.findall('\nFrom: (\S+@\S+)\n', hdr)
        if len(x) >= 1 :
            sender = x[0]
    # normalize the domain name of Email addresses
    sender = fixsender(sender, allsenders) #fixsender('ggolden@umich.edu', allsenders)
    #it was found that none of the emails have 'gmane.org'; so sender = sender
    date = None
    y = re.findall('\nDate: .*, (.*)\n', hdr) #['8 Dec 2005 23:34:30 -0600']
    sent_at = None
    if len(y) >= 1 :
        tdate = y[0] #'8 Dec 2005 23:34:30 -0600'
        tdate = tdate[:26] #'8 Dec 2005 23:34:30 -0600'
        try:
            sent_at = parsemaildate(tdate) #parsemaildate('8 Dec 2005 23:34:30 -0600') = '2005-12-08T23:34:30-06:00'
        except Exception as e:
            # print('Date ignored ',tdate, e)
            return None
    subject = None
    z = re.findall('\nSubject: (.*)\n', hdr) #['call for participation: developers documentation']
    if len(z) >= 1 : subject = z[0].strip().lower() #'call for participation: developers documentation'
    guid = None
    z = re.findall('\nMessage-ID: (.*)\n', hdr) #['<B7EAF76E-3366-4AE3-BDD6-6743707FEBA9@umich.edu>']
    if len(z) >= 1 : guid = z[0].strip().lower() #'<b7eaf76e-3366-4ae3-bdd6-6743707feba9@umich.edu>'
    if sender is None or sent_at is None or subject is None or guid is None :
        return None
    return (guid, sender, subject, sent_at) #('<b7eaf76e-3366-4ae3-bdd6-6743707feba9@umich.edu>', 'ggolden@umich.edu', 'call for participation: developers documentation', '2005-12-08T23:34:30-06:00')
conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Messages ''') #(id, guid, sent_at, sender_id, subject_id, headers, subject_id)
cur.execute('''DROP TABLE IF EXISTS Senders ''') #(id, sender)
cur.execute('''DROP TABLE IF EXISTS Subjects ''') #(id, subject)
cur.execute('''DROP TABLE IF EXISTS Replies ''') #(from_id, to_id)
cur.execute('''CREATE TABLE IF NOT EXISTS Messages
    (id INTEGER PRIMARY KEY, guid TEXT UNIQUE, sent_at INTEGER,
     sender_id INTEGER, subject_id INTEGER,
     headers BLOB, body BLOB)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Senders
    (id INTEGER PRIMARY KEY, sender TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Subjects
    (id INTEGER PRIMARY KEY, subject TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Replies
    (from_id INTEGER, to_id INTEGER)''')
conn_1 = sqlite3.connect('mapping.sqlite')
cur_1 = conn_1.cursor()
cur_1.execute('''SELECT old,new FROM DNSMapping''')
for message_row in cur_1 :
    dnsmapping[message_row[0].strip().lower()] = message_row[1].strip().lower()
mapping = dict()
cur_1.execute('''SELECT old,new FROM Mapping''')
for message_row in cur_1 :
    old = fixsender(message_row[0]) #fixsender('s.swinsburg@lancaster.ac.uk')
    new = fixsender(message_row[1]) #fixsender('steve.swinsburg@swinsborg.com')
    mapping[old] = fixsender(new) # s.swinsburg@lancaster.ac.uk : steve.swinsburg@swinsborg.com
# Done with mapping.sqlite
conn_1.close()
# Open the main content (Read only)
conn_1 = sqlite3.connect('file:content.sqlite?mode=ro', uri=True) #read only
cur_1 = conn_1.cursor()
allsenders = list()
cur_1.execute('''SELECT email FROM Messages''')
for message_row in cur_1 : #adds each sender into allsenders list once, except those with gmane.org
    sender = fixsender(message_row[0])
    if sender is None : continue
    if 'gmane.org' in sender : continue
    if sender in allsenders: continue
    allsenders.append(sender)
print("Loaded allsenders",len(allsenders),"and mapping",len(mapping),"dns mapping",len(dnsmapping))
cur_1.execute('''SELECT headers, body, sent_at
    FROM Messages ORDER BY sent_at''')
senders = dict()
subjects = dict()
guids = dict()
count = 0
for message_row in cur_1 :
    hdr = message_row[0] #selects header even if email has gmane.org in it
    parsed = parseheader(hdr, allsenders) ##('<b7eaf76e-3366-4ae3-bdd6-6743707feba9@umich.edu>', 'ggolden@umich.edu', 'call for participation: developers documentation', '2005-12-08T23:34:30-06:00')
    if parsed is None: continue #None if message_id, sender, subject, or sent_at is None
    (guid, sender, subject, sent_at) = parsed
    # Apply the sender mapping
    sender = mapping.get(sender,sender) #swaps with new email fo the sender if available, otherwise, returns input sender
    count = count + 1 #successfully parsed one email
    if count % 250 == 1 : print(count,sent_at, sender)
    # print(guid, sender, subject, sent_at)
    if 'gmane.org' in sender:
        print("Error in sender ===", sender)
    sender_id = senders.get(sender,None) #looks for sender_id in senders dict
    subject_id = subjects.get(subject,None) #Looks for subject in subjects dict
    guid_id = guids.get(guid,None) #Looks for message_id in guids
    if sender_id is None :
        cur.execute('INSERT OR IGNORE INTO Senders (sender) VALUES ( ? )', ( sender, ) ) #inserts sender into Senders Table
        conn.commit()
        cur.execute('SELECT id FROM Senders WHERE sender=? LIMIT 1', ( sender, )) #gets sender_id
        try:
            row = cur.fetchone()
            sender_id = row[0]
            senders[sender] = sender_id #correlates sender with sender_id
        except:
            print('Could not retrieve sender id',sender)
            break
    if subject_id is None : #copy of sender_id loop abvove
        cur.execute('INSERT OR IGNORE INTO Subjects (subject) VALUES ( ? )', ( subject, ) )
        conn.commit()
        cur.execute('SELECT id FROM Subjects WHERE subject=? LIMIT 1', ( subject, ))
        try:
            row = cur.fetchone()
            subject_id = row[0]
            subjects[subject] = subject_id
        except:
            print('Could not retrieve subject id',subject)
            break
    # print(sender_id, subject_id)
    cur.execute('INSERT OR IGNORE INTO Messages (guid,sender_id,subject_id,sent_at,headers,body) VALUES ( ?,?,?,datetime(?),?,? )',
            ( guid, sender_id, subject_id, sent_at,
            zlib.compress(message_row[0].encode()), zlib.compress(message_row[1].encode())) )
            #header and body are compressed using zlib, then encoded into bytes/unicode
    conn.commit()
    cur.execute('SELECT id FROM Messages WHERE guid=? LIMIT 1', ( guid, ))
    try:
        row = cur.fetchone()
        message_id = row[0]
        guids[guid] = message_id #guid is the email message_id, while the message_id is the table message_id
    except:
        print('Could not retrieve guid id',guid)
        break
cur.close()
cur_1.close()

#gbasic.py
import sqlite3
import time
import zlib
howmany = int(input("How many to dump? "))
conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()
cur.execute('SELECT id, sender FROM Senders')
senders = dict() # sender_id : sender
for message_row in cur :
    senders[message_row[0]] = message_row[1] # id : sender
cur.execute('SELECT id, subject FROM Subjects')
subjects = dict() # subject_id : subject
for message_row in cur :
    subjects[message_row[0]] = message_row[1]
# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages') # collected to show total amount of each, and to count senders and org
messages = dict() # message_id : (guid, sender_id, subject_id, sent_at)
for message_row in cur :
    messages[message_row[0]] = (message_row[1],message_row[2],message_row[3],message_row[4])
print("Loaded messages=",len(messages),"subjects=",len(subjects),"senders=",len(senders))
sendcounts = dict()
sendorgs = dict()
for (message_id, message) in list(messages.items()):
    sender = message[1] #sender_id
    sendcounts[sender] = sendcounts.get(sender,0) + 1 #sendcounts records the number of counts for each sender_id; len(sendcounts) = len(senders)
    pieces = senders[sender].split("@") #['csev', 'umich.edu']
    if len(pieces) != 2 : continue
    dns = pieces[1] #'umich.edu'
    sendorgs[dns] = sendorgs.get(dns,0) + 1 #sendcounts records the number of counts for each organization; len(sendorgs) = len(senders)
print('') #creates new line
print('Top',howmany,'Email list participants')
x = sorted(sendcounts, key=sendcounts.get, reverse=True) #returns sorted keys list
#sorted(sendcounts) sorts the dict based on the keys from lowest to highest, returns sorted keys
#sorted(sendcounts, key=sendcounts.get) sorts based on the values from lowest to highest, but returns sorted keys
for k in x[:howmany]:
    print(senders[k], sendcounts[k])
    if sendcounts[k] < 10 : break
print('')
print('Top',howmany,'Email list organizations')
x = sorted(sendorgs, key=sendorgs.get, reverse=True)
for k in x[:howmany]:
    print(k, sendorgs[k])
    if sendorgs[k] < 10 : break

#gword.py
import sqlite3
import time
import zlib
import string
conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()
cur.execute('SELECT id, subject FROM Subjects')
subjects = dict() # subject_id : subject
for message_row in cur :
    subjects[message_row[0]] = message_row[1]
# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('SELECT subject_id FROM Messages')
counts = dict() # word: word_count
for message_row in cur :
    text = subjects[message_row[0]] #subject
    text = text.translate(str.maketrans('','',string.punctuation))
    #string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #str.maketrans('','',stringpunctuation) creates a dict (ASCII value : None) with all punctuation characters
    #the first input are the old characters being changed; the second input are the corresponding new characters; the last input is being removed
    #the first and second inputs must be the same size
    #text.translate(str.maketrans('','',string.punctuation)) does the changing within 'text'
    text = text.translate(str.maketrans('','','1234567890')) #removes all numbers
    text = text.strip()
    text = text.lower()
    words = text.split()
    for word in words:
        if len(word) < 4 : continue #word length filter
        counts[word] = counts.get(word,0) + 1 #counts every single word in all subjects
x = sorted(counts, key=counts.get, reverse=True)[:100] #outputs word list in order to highest to lowest counts; top 100
#gets the highest and lowest counts within the top 100 words
highest = counts[x[0]]
lowest = counts[x[99]]
print('Range of counts:',highest,lowest)
# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20
fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()
print("Output written to gword.js")
print("Open gword.htm in a browser to see the visualization")

#gline.py
import sqlite3
import time
import zlib
conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()
cur.execute('SELECT id, sender FROM Senders')
senders = dict() # sender_id : sender
for message_row in cur :
    senders[message_row[0]] = message_row[1]
cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
messages = dict() # id : (guid, sender_id, subject_id, sent_at)
for message_row in cur :
    messages[message_row[0]] = (message_row[1],message_row[2],message_row[3],message_row[4])
print("Loaded messages=",len(messages),"senders=",len(senders)) #prints number of messages and senders
sendorgs = dict()
for (message_id, message) in list(messages.items()):
    sender = message[1] #sender_id = 1
    pieces = senders[sender].split("@") #['ggolden22', 'mac.com']
    if len(pieces) != 2 : continue
    dns = pieces[1] #'mac.com'
    sendorgs[dns] = sendorgs.get(dns,0) + 1 #counts each organization
# pick the top schools
orgs = sorted(sendorgs, key=sendorgs.get, reverse=True) #list of top organization names based on count; highest to lowest
orgs = orgs[:10] #top 10
print("Top 10 Organizations")
print(orgs)
counts = dict()
months = list()
# cur.execute('SELECT id, guid,sender_id,subject_id,sent_at FROM Messages')
for (message_id, message) in list(messages.items()):
    sender = message[1] #sender_id = 1
    pieces = senders[sender].split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1] #'mac.com'
    if dns not in orgs : continue
    month = message[3][:7] #gets 'sent_at'; '2005-12'
    if month not in months : months.append(month)
    key = (month, dns) #('2005-12', 'mac.com')
    counts[key] = counts.get(key,0) + 1 #counts month+top10org combination for each message
months.sort() #sorts list form lowest to highest
fhand = open('gline.js','w')
fhand.write("gline = [ ['Month'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")
for month in months:
    fhand.write(",\n['"+month+"'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");
fhand.write("\n];\n")
fhand.close()
print("Output written to gline.js")
print("Open gline.htm to visualize the data")
