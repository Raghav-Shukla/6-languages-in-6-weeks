import time
import threading
import sys

i=0
start=0
def loop():
    global start
    start=time.time()    # Initialises the timer
    global i
    while(1):
        i+=1

t2 = threading.Thread(target=loop, name='t2')
t2.start()
while(1):
    if(time.time()-start>1):       #Checks for 1 second
        print(time.time()-start)
        print(i)
        sys.exit
        break
