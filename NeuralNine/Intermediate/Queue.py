import queue # thread-friendly way of extracting informatio
# prevents skipping or repeating multiple elements as when using a counter variable 
# First-In-First-Out by default
# We can change it to Last-In-First-Out

q = queue.Queue()

for i in range(1,11):
    q.put(i)

print(q.get())




q = queue.LifoQueue()

for i in range(1,11):
    q.put(i)

print(q.get())




q = queue.PriorityQueue() # Ordered bases on priority ; Lowest-Priority-First-Out
q.put((2, "Hello World!"))
q.put((11, "Hello"))
q.put((5, "Nice"))

while not q.empty():
    print(q.get()[1])
