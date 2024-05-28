# Important for checking contents of collections of lists/sequences

any([True, False]) 
# Returns True if any element returns True

all([True, False])
# Returns True if all elements return True

x = [True, True, False, True]
print(any(x), all(x))

nums = [11,12,76,55,9,88,10]
even = lambda x: x%2 ==0

# They are the same list of True's and False's
FTlst = list(map(even, nums))
res = [i%2==0 for i in nums]

print("At least one number is even" if any(res) else "No number is even!")
if all(res): print("All numbers are even")