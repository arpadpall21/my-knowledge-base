# import asyncio

# async def sayHi(name, delay):       # corutine
#     await asyncio.sleep(delay)
#     print( "Hello World!" )
#     return f"{name} result"

# async def main():
#     result = await asyncio.gather(sayHi('one', 1), sayHi('two', 1.5))     # starts both corutines and awaits their results
#     print( result )               # // -> ['one result', 'two result']

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def sayHi(name, delay):       # corutine
#     await asyncio.sleep(delay)
#     print( "Hello World!" )
#     return f"{name} result"

# async def main():
#     task1 = asyncio.create_task(sayHi('one', 1))        # once tasks are created immediately starts executing its corutine in the background   
#     task2 = asyncio.create_task(sayHi('two', 1.5))
    
#     print( await task1 )            # // -> "one result"    # awaiting task results 
#     print( await task2 )            # // -> "two result"

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def listGen():
#     yield 1
#     yield 2
#     yield 3

# async def main():
#     async for i in listGen():
#         print( i )

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def listGen():
#     yield 1
#     yield 2
#     yield 3

# async def main():
#     result = [i async for i in listGen()]
#     print( result )

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def sayHi():
#     await asyncio.sleep(5)
#     return 'some result'

# async def main():
#     task1 = asyncio.create_task(sayHi())
#     await asyncio.shield(task1)                 # shiled the task from cancellation
    
#     task1.cancel()                              # ignored because the task in shielded
    
#     print( await task1 )                        # // -> 'some result'

# asyncio.run(main())

########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def sayHi():
#     await asyncio.sleep(1)
#     return 'some result'

# async def main():
#     print( await asyncio.wait_for(sayHi(), timeout=2))    # // -> "some result"
#     print( await asyncio.wait_for(sayHi(), timeout=.1))   # // -> asyncio.exceptions.TimeoutError

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def sayHi(name, delay):
#     await asyncio.sleep(delay)
#     return f"{name} result"

# async def main():
#     task1 = asyncio.create_task(sayHi('one', 1))
#     task2 = asyncio.create_task(sayHi('two', 2))
#     task3 = asyncio.create_task(sayHi('three', 3))
#     result = await asyncio.wait([task1, task2, task3])

    # for i in result[0]:           # finished tasks
    #     print( await i )          # // -> "two result"  |  "one result"  |  "three result"


# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def sayHi(name, delay):
#     await asyncio.sleep(delay)
#     return f"{name} result"

# async def main():
#     task1 = asyncio.create_task(sayHi('one', 1))
#     task2 = asyncio.create_task(sayHi('two', 2))
#     task3 = asyncio.create_task(sayHi('three', 3))
#     result = asyncio.as_completed([task1, task2, task3])

#     for i in result:              # genObj yields the result as soon as they finished
#         print( await i )          # // -> "one result"  |  "two result"  |  "three result"

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio
# import time

# def blockingIo(name, delay):
#     print( f'blocking io {name} start' )
#     time.sleep(delay)
#     print( f'blocking io {name} end!' )

#     return 'blocking io result'

# async def main():
#     print( await asyncio.to_thread(blockingIo, 'one', 1.2) )        # "blocking io result"


# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def someCoro(name, delay):
#     await asyncio.sleep(delay)
#     return f'coro {name} result'

# async def main():
#     task1 = asyncio.Task(someCoro('one', 1.3))

#     print( await task1 )        # // -> "coro one result"

# asyncio.run(main())


########################################################################################
########################################################################################
########################################################################################

# import asyncio

# async def someCoro(name, delay):
#     await asyncio.sleep(delay)
#     return f'coro {name} result'

# async def main():
#     task = asyncio.Task(someCoro('one', 1.3))

#     print( await task )             # // -> "coro one result"

#     print( task.cancelled() )       # // -> False
#     print( task.result() )          # // -> "coro one result"


# asyncio.run(main())

########################################################################################
########################################################################################
########################################################################################

import asyncio

async def someCoro(delay):
    await asyncio.sleep(delay)
    raise ValueError('some exception')


async def main():
    task = asyncio.Task(someCoro(1.3))

    print( task.exception() )

asyncio.run(main())
