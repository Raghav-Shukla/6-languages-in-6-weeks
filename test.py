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
    t=time.time()-start
    if(t>=1):       #Checks for 1 second
        print(t)
        print(i)
        sys.exit
        break
