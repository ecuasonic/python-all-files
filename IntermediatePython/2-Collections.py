# collections: ____________________________________________________________________________________________________________________________________________________________________________
# implements special containter types;
# Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
str = 'aaabbbBbbcccc'
my_counter = Counter(str) #Counter({'a':4, 'b':4, 'c':4})
items = my_counter.items() #dict_items([('a',4),('b',4), ('c',4)],)
keys = my_counter.keys() #dict_keys(['a','b','c'])
values = my_counter.values() #dict_calues([4,4,4])
val = my_counter.most_common() #[('b',5),('c',4),('a',3),('B',1)]
val = my_counter.most_common(3) #[('b',5),('c',4),('a',3)]; includes top 3 characters; akin to dict.items()
ele = my_counter.elements() #<itertools.chain object at 0x000002CC02186F50>
lst = list(my_counter.elements()) #['a','a','a','b','b','b','b','b','B','c','c','c','c']


from collections import namedtuple
Point = namedtuple('Point','x,y') #this will create a class called Point with fields x and y 
pt = Point(1,-4) #Point(x=1, y=-4)
pt.x #1
pt.y #-4


from collections import OrderedDict #may be a way to use a dictionary that rememebers order in older version of Python; Python 3.7 and beyond already do this in dict regular
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 1
ordered_dict['c'] = 1 #OrderedDict([('a',1),('b',1),('c',1)])


from collections import defaultdict
d = defaultdict(int) #integer as default type
d['a'] = 1
d['b'] = 2 #defaultdict(<class 'int'>, {'a':1, 'b':2})
d['b'] #2
d['c'] #0; default value for integer; 0.0 default value for floats, [] for lists, etc.


from collections import deque
d = deque()
d.append(1)
d.append(2) #deque([1,2])
d.appendleft(3) #deque([3,1,2])
d.pop() #deque([3,1])
d.popleft() #deque([1])
d.clear() #deque([])
d.extend([4,5,6]) #deque([4,5,6])
d.extendleft([3,2,1]) #deque([1,2,3,4,5,6]) ; appends in order, and not all at once ; left side of input list goes in first
d.rotate(1) #deque([6,1,2,3,4,5]); rotates to the right
d.rotate(-2) #deque([2,3,4,5,6,1]); rotates to the left