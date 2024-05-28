import json

#https://www.python-engineer.com/courses/advancedpython/11-json/

'''{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "hasChildren":true,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}'''

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSN = json.dumps(person, indent = 4, sort_keys=True) #separators=('; ', '= ')
#converts dictionary to JSON string
#sort_keys = True ; sorts the dictionary alphabetically
#separators = (': ', '= ') ; changes the ":' to "=" and "," to ";"

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
#json.dump is different from json.dumps, since (dump) gets JSON to file, while (dumps) gets JSON to string

person = json.loads(personJSN)
#converts JSON string to dictionary

with open('person.json', 'r') as file:
    person = json.load(file)
#json.load is different from json.loads, since (load) gets JSON from file, while (loads) gets JSON from string

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o,User):
    #isinstance(object, class) returns true or false
        return {"name": o.name, "age": o.age, o.__class__.__name__: True} 
        #o.__class__.__name__ prints out the class name, which is "User" in this case
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o): #This overrides the current default function in JSONEncoder
        if isinstance(o,User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True} 
        return JSONEncoder.default(self,o) #runs the current default function if object is not an instance of User class

userJSON = json.dumps(user, default=encode_user) #json.dumps(encode_user(user))
userJSON = json.dumps(encode_user(user))
userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
#This converts the user object to a JSON string with the help of user-created encode_user function
print(userJSON)

def decode_user(dct):
    if dct['User']: #if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"]) #return User(dct["name"], dct["age"])
    return dct

user = json.loads(userJSON, object_hook=decode_user) #loads the userJSON string into a User object instead of a dictionary
print(user.name)

