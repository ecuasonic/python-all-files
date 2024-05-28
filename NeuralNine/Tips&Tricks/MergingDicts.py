dict1 = {'a':1, 'b':7}
dict2 = {'b':4, 'c':8}

#UPDATE ; Changes already present items and adds new items
#dict1.update(dict2)
#print(dict1)

#dict3 = dict(**dict1, **dict2) ; ERROR, both are added at the same time, can't have keys with multiple values
dict3 = {**dict1, **dict2} # last one added updates the existing keys
dict4 = {**dict2, **dict1}
print(dict3, dict4)

#MERGING operator
dict5 = dict1|dict2
print(dict5)

#UPDATE operator
#dict6 = dict1 |= dict2
print(dict5)

