# This is comparable to the (?) operator in JAVA programming lang
# Used to make "if" statements more concise and elegant

age = 12

if age >= 18:
    adult = True
else:
    adult = False

if adult:
    print("You are an adult!")
else:
    print("You are not an adult!")



age = 18

adult = True if age >= 18 else False

print("You are an adult!" if adult else "You are not an adult!")



# Multiple Ternary Operators
number = 2000
print("Very very large!" if number > 1000 
      else "Quite large!" if number > 100 
      else "Small but still positve!" if number > 0 
      else "Not positive!")