import threading

def fun1():
    for i in range(10):
        print("Hey guys")
def fun2():
    for i in range(14):
        print("WYD?")        

t1=threading.Thread(target=fun1)


t2=threading.Thread(target=fun2)

t1.start()
t2.start()
