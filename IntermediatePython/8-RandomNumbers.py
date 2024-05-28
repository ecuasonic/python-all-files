import random #used to generate psuedo-random numbers for various distributions
#pseudo random, because they are reproducable

a = random.random() # float[0,1)

a = random.uniform(1,10) # float[1,10]

a = random.randint(1,10) # int[1,10]

a = random.randrange(1,10) # int[1,9]

a = random.normalvariate(0,1) # mu (mean) = 0, sigma (standard deviation) = 1, bell-shaped curve

mylist = list('ABCDEFGH')
a = random.choice(mylist) #picks an element from mylist
a = random.sample(mylist,3) #picks 3 unique elements from mylist
a = random.choices(mylist, k=3) #picks any (not unique restricted) elements from mylist
random.shuffle(mylist) #shuffles mylist randomly

random.seed(1) # sets all random objects/methods to a single iteration of randomness
#all random offspring are set constant now and are reproducable
print(random.random())
print(random.randint(1,10))
print(mylist)

import secrets
#should be used for passwords, security tokens, account authentication 
#this will generate a true random number

a = secrets.randbelow(10) # int[0,10)

a = secrets.randbits(4) #can have 4 different random binary numbers, which add up to 15 ; int[0,15]

mylist = list("ABCDEFG")
a = secrets.choice(mylist) #picks an element from mylist

import numpy as np
#to make arrays with random elements

a = np.random.rand(3,3) # n by n array with random elements

a = np.random.randint(0,10,(2,3)) # [0,10) ; makes 2x3 array with random integers as elements

arr = np.array([[1,2,3],[4,5,6],[7,8,9]]) #creates array
np.random.shuffle(arr) #randomly shuffles array rows

np.random.seed(1) # works similarly to random.seed(1); another psuedo-random generator
print(np.random.rand(4,4)) 



