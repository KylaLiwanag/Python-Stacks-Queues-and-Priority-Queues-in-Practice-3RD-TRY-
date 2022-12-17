#1st Example Representing Priority Queues With a Heap
from heapq import heappush

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)


#2nd Example Representing Priority Queues With a Heap
from heapq import heappop

print(heappop(fruits))


print(fruits)

#3rd Example Representing Priority Queues With a Heap

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)

print(person2 < person3)