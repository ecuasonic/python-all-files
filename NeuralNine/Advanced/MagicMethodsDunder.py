import time
class Vector:

    def __init__(self, x, y): # constuctor class ; called when an object is created
        self.x = x
        self.y = y
        self.data = {}
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self): # represents the object as it is in the code, whether by itself or in a list ; if __str__ is not defined, then __repr__ takes it place ; still an object
        # Called by the repr() function to get the "official" string representation of an object
        # Should be unambiguous and ideally can be used to recreate the object
        return f'Vector(x={self.x}, y={self.y})'
    
    def __str__(self): # called when str(object) or print(object) is called
        return f"X: {self.x}, Y: {self.y}"
    
    def __len__(self): # called when len(object) is called
        return len(self.data)
    
    def __call__(self): # called when object is called
        print("Hello! I was called!")
        return "Printed"
        
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        if self.x == other.x and self.y == other.y:
            print("They are equal!")
            return True
        return False
        
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return False
        if self.x < other.y and self.y < other.y:
            print(f"{self} is less than {other}")
            return True
        print(f"{self} is not less than {other}")
        return False
    
    def __gt__(self, other):
        if not isinstance(other, Vector):
            return False
        if self.x > other.y and self.y > other.y:
            print(f"{self} is greater than {other}")
            return True
        print(f"{self} is not greater than {other}")
        return False
    
    def __getitem__(self, key): # called when you access an item in an object using square brackets, obj[key]
        # When the v4[key] is on the right side
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        return self.data[key]
        
    def __setitem__(self, key, value): # Enables objects to support assignment of items using indexing (obj[key] = value
        # When the v4[key] is on the left side
        print(f'Setting {key} to {value}')
        self.data[key] = value # adds key:value pair to the object dictionary

    def __contains__(self, key):
        print(f"Checking if {key} is in the list.")
        return key in self.data # returns boolean whether key is found in object's dict
    
    def __enter__(self): # what to do when entering "with" block
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback): # what to do when exiting "with" block
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")

    def __delitem__(self,key):
        print(f'{key} has been removed from obj dict')
        del self.data[key]

    def __iter__(self): # initializes the variables used to generate the sequence and returns the instance itself as an iterator
        # called in the beginning of "for _ in v4"
        # called when an iterator object is created
        self.a, self.b = 0,1
        self.count = 0
        return self
    
    def __next__(self): # calculates the next fibonacci number in the sequence until the specified limit is reached
        # called after each iteration of "for _ in v4"
        # called each time the next element from the iterator is requested
        # uses the next() function
        if self.count < 10: 
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration
        
    # __sub__, __mul__, __div__, __floordiv__, __mod__, __pow__
    # __ne__, __le__, __ge__

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


    
v1 = Vector(10,15)
v2 = Vector(1,0)
v3 = v1 + v2
print(v3)
print(str(v3))
print(repr(v3))
v4 = eval(repr(v3)) # creates copy 
print(len(v3))
print(v3())
v4 == v3
v4 < v3
v4 > v3
print(v4[0], v4[1])
v4[0] = 12
print(v4[0], v4[1]) # unchanged, because __getitem__ refers to self.x when looking for key=0, and not in the obj dict
v4[2] = 'item'
print(2 in v4)

def time_consuming_operation():
    total = 0
    for i in range(100000):
        total += i
    print("Operation completed!")

with v4 as v:
    time_consuming_operation()

print(v4.data)
del v4[2]
print(v4.data)

for i in v4:
    print(i)

