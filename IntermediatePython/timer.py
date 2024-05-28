from timeit import default_timer as timer
start = timer()
lst = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(1000000):
    lst.reverse()
stop = timer()
print(stop-start)
start = timer()
for i in range(1000000):
    lst = lst[::-1]
stop = timer()
print(stop-start)