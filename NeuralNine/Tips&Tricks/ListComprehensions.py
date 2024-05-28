numbers = [18,16,22, 99, 23]
evens = [i for i in numbers if i%2==0]
odds = [i for i in numbers if i%2==1]
pow2 = [i*i for i in numbers]
pow2ex = [i*i for i in range(30)]
print(evens, odds, pow2, pow2ex)

words = ['automobile', 'car', 'anger', 'fox']
upper = [w.upper() for w in words if w.startswith('a')] # 'exp' 'for loop' 'if...cond'
upper = [w.upper() if w.startswith('a') else w for w in words] # 'exp' 'if...else' 'for loop' ; outputs 'exp' 'if...cond', otherwise outputs 'else'
# upper = [w.upper() for w in words if w.startswith('a') else w]
# upper = [w.upper() if w.startswith('a') for w in words]
print(upper)

lst1 = [1,2,3]
lst2 = ['a', 'b', 'c', 'de']
lst = [str(x)+y for x in lst1 for y in lst2] # 'str(x)+y for x in lst1' counts as an expression involving y in lst2
lst = [str(x)+y for x in lst1 if x<2 for y in lst2 if len(y)==1]
lst = [[x*y for x in lst1] for y in lst2] # creates lists within lst

d1 = dict(k1=1, k2=2, k3=3)
d2 = {key:value**2 for key,value in list(d1.items())}
d3 = {x**3:y.upper() for x,y in zip(lst1,lst2)}
print(d3)