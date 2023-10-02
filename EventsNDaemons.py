import threading

event=threading.Event()

def fun1():
    print("waiting for the event to trigger\n")
    event.wait()
    print("Performing action XYZ now....\n")
t1=threading.Thread(target=fun1)
t1.start()

x=input("Do you want to trigger the function?(Y/N)\n")  
if x=="Y":
    event.set()  #launching the event
