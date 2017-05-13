import asyncio
from random import randint

def yoda_says(future):
    res = future.result()
    res.sort()
    print("Or, as Yoda would say, '{}'".format(' '.join(res)))
    loop.stop()
    
async def other_func(future):
    words = ['PyAugusta', 'is', 'for', 'Python']
    for i in words:
        await asyncio.sleep(randint(1, 3))
        print(i)
    future.set_result(words)
        
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(other_func(future))
    future.add_done_callback(yoda_says)
    try:
        loop.run_forever()
    finally:
        loop.close()