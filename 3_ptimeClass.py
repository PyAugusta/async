import time
from random import randint

class pTime(object):

    def __init__(self, sleep_low, sleep_high):
        self.sleep_low = sleep_low
        self.sleep_high = sleep_high
        
    def run(self):
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
    ptime = pTime(1, 4)
    ptime.run()
    other_func()