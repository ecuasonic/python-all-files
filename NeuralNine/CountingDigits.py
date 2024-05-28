num = 999999999999999999999999999999997
print(len(str(num)))

#NO TYPE-CASTING
import math
print(math.ceil(math.log10(abs(num))))

counter = 1
while abs(num) >= (10**counter):
    counter += 1
print(counter)