import threading
import time

path="Reader.txt"
text=""

def readFile():
    global path,text
    while True:
        with open("Reader.txt","r") as f:
            text=f.read()
            time.sleep(3)
def printloop():
    for x in range(15):
        print(text)
        time.sleep(1)
t1=threading.Thread(target=readFile,daemon=True) #declaring that readfile be a Daemon thread that will always be running in the background
t2=threading.Thread(target=printloop)

t1.start()     
t2.start()              
