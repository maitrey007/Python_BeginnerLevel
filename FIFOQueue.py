import queue
 
q=queue.Queue()#creating a queue

numbers=[1,2,3,4,5,66]
for i in numbers:
    q.put(i)
print(q.get())   
