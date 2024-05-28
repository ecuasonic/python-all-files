name = "Mike"
age = 25
num = 19.84928149038214

print("Hello my name is " + name + " and I am " + str(age) +  " years old!")
print("Hello my name is %s and I am %d years old! My fav number is %.2f" % (name,age,num))
print("Hello my name is {} and I am {} years old! My fav number is {:.2f}".format(name,age,num))
print(f"Hello my name is {name} and I am {age if age % 2 == 0 else 7} years old! My fav number is {num:.2f}")
