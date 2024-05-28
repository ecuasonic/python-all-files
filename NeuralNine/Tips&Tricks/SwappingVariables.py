a = 10
b = 20

print(a,b)
temp = a
a = b
b = temp
print(a, b)
a,b = b,a # Works with multiple variable swaps
print(a,b)

a = 10
b = 20
'''
24 = 011000 -> a
41 = 101001 -> b
     110001 -> MASK = a XOR b
     MASK XOR b -> a

XOR
'''
print(a,b)
a = a^b # a -> a_og XOR b_og == MASK
b = b^a # b -> b_og XOR MASK == a_og
a = a^b # a -> MASK XOR a_og == b__og
print(a,b)
