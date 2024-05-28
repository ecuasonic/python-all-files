import statistics as s

lst = [
2,3,4,5,6,7,8,9,100
]

print(f"mean: {s.mean(lst)}")
print(f"Q1: {s.quantiles(lst)[0]}")
print(f"median: {s.median(lst)}")
print(f"Q3: {s.quantiles(lst)[2]}")
print(f"s: {s.stdev(lst):.3f}")
# s = sqrt(sum(diff**2)/(n-1))