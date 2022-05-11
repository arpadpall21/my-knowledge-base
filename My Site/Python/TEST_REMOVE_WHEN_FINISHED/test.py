import asyncio

async def delay(delay):
    await asyncio.sleep(delay)
    print( f'Delayed {delay} seconds')
    return 'OK'

async def main():
    # loop = asyncio.get_event_loop()
    # future = loop.create_future()
    
    
    task1 = asyncio.create_task(delay(3))
    task2 = asyncio.create_task(delay(3))
    task3 = asyncio.create_task(delay(3))
# 
    print( await asyncio.wait([task1, task2, task3]) )

# asyncio.create_future()
asyncio.run(main())