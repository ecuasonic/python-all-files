import numpy
import cv2
import matplotlib.pyplot as plt

# Question 1
# part a
A = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print('1)a)\n',A)

# part b
B = A[:,2]
print('1)b)\n',B)

#part c
C = A[1]
print('1)c)\n',C)

#part d
print('1)b)\n','They are not the same since the index starts at 0 instead of 1')

#part e
print('1)e)\n', sum(B[:2]))


# Question 2
A = numpy.ones(shape=[3,3] )*5
print('2)\n',A)

# Question 3
A = numpy.random.rand(2,4)
print('3)\n',A)

# Question 4
B = numpy.array([[1,2],[3,4]])
top = numpy.concatenate((B,B),axis = 1)
bottom = numpy.concatenate((B+4,B-1),axis=1)
C = numpy.concatenate((top, bottom), axis=0)
print('4)\n',C)

# Question 5
A = numpy.delete(C, 1, axis=1)
print('5)\n',A)

# Question 6
A = C[1:3,1:3]
print('6)\n',A)

# Question 7
B = [[5,1,2],[3,9,4],[7,6,8]]
