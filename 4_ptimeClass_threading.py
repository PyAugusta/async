import threading
import time
from random import randint

class pTime(threading.Thread): # subclass Thread

    def __init__(self, sleep_low, sleep_high):
        self.sleep_low = sleep_low
        self.sleep_high = sleep_high
        threading.Thread.__init__(self) # initialize the Thread object
        
    def run(self): # overwrite the Thread.run() method
        count = 0
        while count < 5:
            time.sleep(randint(self.sleep_low, self.sleep_high))
            print(time.ctime(time.time()))
            count += 1
            
def other_func():
    for i in ['PyAugusta', 'is', 'for', 'Python']:
        print(i)
        time.sleep(randint(1, 3))


if __name__ == '__main__':
    # create out pTime object, which is a subclass of threading.Thread
    ptime = pTime(1, 4)
    
    # call the start() method, which is part of the threading.Thread object
    # we inherited. This method will call the run() method we wrote, but
    # in a new thread
    ptime.start()
    
    # call out other function
    other_func()
    
    # use the join method to let the thread finish before our program exits
    ptime.join()