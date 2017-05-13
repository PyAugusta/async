import threading
import time
from random import randint

def ptime():
    count = 0
    while count < 5:
        time.sleep(randint(1, 3))
        print(time.ctime(time.time()))
        count += 1

def other_func():
    for i in ['PyAugusta', 'is', 'for', 'Python']:
        time.sleep(randint(1, 3))
        print(i)


if __name__ == '__main__':
    # create a Thread object, passing in our target function
    t = threading.Thread(target=ptime)
    
    # start the thread
    t.start()
    
    # call our other function
    other_func()
    
    # use the join method to let the thread finish before our program exits
    t.join()