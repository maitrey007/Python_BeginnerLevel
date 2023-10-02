import queue
 
q=queue.PriorityQueue()#creating a queue

q.put((12,"Hello world"))
q.put((2,34))
q.put((4,5.5))
q.put((1,True))

print(q.get())
print(q.get())
