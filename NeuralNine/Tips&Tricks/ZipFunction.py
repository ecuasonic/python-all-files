names = ['Anna', 'John', 'Bob', 'Mike', 'July']
ages = [17,22,88,34,53]

for i in range(len(names)):
    print(f"Name: {names[i]}, Age: {ages[i]}")

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")



# Operations for each zipped element
sales = [500,800,300,1200,600]
costs = [200,600,200,100,800]

for sale, cost in zip(sales, costs):
    print(sale-cost)



# Unzipping
#     zip(tuple1, tuple2, ...) unzips the indexed elements into seperate tuples
#     zip(list1, list2, ...) zips the indexed elements into a tuple within a list
zipped = [('Mike', 50), ('Bob', 20), ('Anna', 70), ('John', 35)]
names, ages = zip(*zipped) # returns two tuples of names and ages
print(list(names), list(ages))



# Sorting two psuedo-connected lists 
lets = ['b','d', 'a', 'c']
nums = [3,2,4,1]
data = sorted(zip(lets, nums))
lets_new, nums_new = zip(*data)
print(list(lets_new), list(nums_new))



# Converting two lists to a dictionary
mydict = dict(zip(lets, nums))
print(mydict)