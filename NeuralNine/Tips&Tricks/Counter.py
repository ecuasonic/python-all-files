lst = [1,2,3,3,1,5,4,1,4,3,2,1,4,3,2,1,4,3,1,2,3,4,3,2,1,4,3,1,2,4,3,1,2,4]

current_max = 0
current_val = None
for x in set(lst):
    if lst.count(x) > current_max:
        current_max, current_val = lst.count(x), x
print(f"Value: {current_val}, Frequency: {current_max}")




from collections import Counter

counter = Counter(lst)
x = counter.most_common(1)[0]
print(f"Value: {x[0]}, Frequency: {x[1]}")




current_val = max(lst, key = lst.count) # Performs lst.count() for ALL elements
print(f"Value: {current_val}, Frequency: {lst.count(current_val)}")

current_val = max(set(lst), key = lst.count) # Performs lst.count() for non-repeating elements
print(f"Value: {current_val}, Frequency: {lst.count(current_val)}")