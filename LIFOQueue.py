import queue
 
q=queue.LifoQueue()#creating a queue

numbers=[1,2,3,4,5,66]
for i in numbers:
    q.put(i)
print(q.get(i))
print(q.get(i))
# this  queue is the LIFO queue
