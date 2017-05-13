# python > 3.5
import asyncio
import time
from random import randint

async def ptime():
    count = 0
    while count < 5:
        await asyncio.sleep(randint(1, 3))
        print(time.ctime(time.time()))
        count += 1
        
async def other_func():
    for i in ['PyAugusta', 'is', 'for', 'Python']:
        await asyncio.sleep(randint(1, 3))
        print(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        ptime(),
        other_func()
    ))
    loop.close()