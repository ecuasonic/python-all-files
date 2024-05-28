# Application 1 : Seq 1 to 9000 and cube each one
import sys
lst = []
for x in range(9000): # Creates the object all at once
    lst.append(x**3)

def mygen(n): # Provides the instructions of how to proceed ; n is used to create a boundary ; each iteration is saved, however
    # Very useful in algorithmic processing of large datasets and memory efficiency ; also in sequential processing
    for x in range(n):
        yield x**3

values = mygen(100)

print(lst.__sizeof__())
print(sys.getsizeof(lst))
print(values.__sizeof__())
print(sys.getsizeof(values))

print(next(values))
print(next(values))
print(next(values))

for x in values:
    print(x)

def inf_seq():
    result = 1
    while True:
        yield result
        result *= 5

values = inf_seq()
print(next(values))
print(next(values))
print(next(values))

