# Enumuation is very useful to index data when not indexed yet 
names = ['John', 'Anna', 'Bob', 'Sarah']

counter = 0
for name in names:
    print(f"{counter}: {name}")
    counter += 1

print(list(enumerate(names))) # creates a list of tuples with 'names' element and index 

for index, name in enumerate(names):
    print(f"{index}: {name}")