numbers = [14,23,8,12,2]

def square(x):
    return x*x

lst = [square(i) for i in numbers]
lst = list(map(square, numbers)) # need to type-cast into list
# performs the function for each element in the list

print(lst)