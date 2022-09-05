# import concurrent.futures
# import time

# r = 10000000
# start = time.time()

# def countrange(name, len):
#     for i in range(len + 1):
#         if i == r / 4:
#             print( f"{name}: {i}" )
#         elif i == r / 2:
#             print( f"{name}: {i}" )
#         elif i == r / 4 * 3:
#             print( f"{name}: {i}" )
#         elif i == r:
#             print( f"{name}: {i}" )

# def th(name, b):
#     print(f'{name} started')
#     countrange(name, r)
#     print(f'{name} end!')
#     print( f'2nd argument {b}')



# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     executor.map(th, ['Thread-1', 'Thread-2', 'Thread-3'], ['x', 'y', 'z'])




# print( f"Running time: {time.time() - start}" )


###############################################################################################
###############################################################################################
###############################################################################################

# from concurrent.futures import ThreadPoolExecutor
# import threading

# lock = threading.RLock()
# threadpolExecutor = ThreadPoolExecutor(max_workers=5)

# def countrange(name, loop):
#     if loop:
#         for i in range(10000000):
#             pass

# def th(name, lock, loop=True):
#     print(f'{name} started')
#     with lock:                      # lock supports context protocol 
#         countrange(name, loop)      # lock unlocket at the start of the context and locked at the end of it
#     print(f'{name} end!')

# threadpolExecutor.map(th, ['th-1', 'th-2', 'th-3', 'th-4', 'th-5'], [lock, lock, lock, lock, lock], [False, False, True, False, True])   # start threads
# # threads run concurently but have to wait each other to finish



###############################################################################################
###############################################################################################
###############################################################################################

# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time

# executor = ThreadPoolExecutor(max_workers=2)
# b = threading.Barrier(2)

# # def th():
# #     print( 'th-1 start:' )
# #     time.sleep(1)
# #     b.wait()
# #     print( 'th-1 end:' )

# def th(name, wait):
#     print( f'{name} start' )
#     time.sleep(wait)
#     b.wait()
#     print( f'{name} end' )

# executor.map(th, [1, 2, 3, 4, 5], [2, 5, 1.2, 1.1, 4.2])


###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################


# import multiprocessing
# import time

# start = time.time()


# def task(name):
#     for i in range(100000001):
#         if i == 100000000:
#             print( f'thread {name} end!' )


# p1 = multiprocessing.Process(target=task, args=[1])
# p2 = multiprocessing.Process(target=task, args=[2])
# p3 = multiprocessing.Process(target=task, args=[3])

# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()

# print( time.time() - start )


###############################################################################################
###############################################################################################
###############################################################################################

# import multiprocessing


# if __name__ == "__main__":
#     multiprocessing.set_start_method('forkserver')

# def pc(name):
#     print( f"{name} process started")

#     print( f"{name} process ended")

# prc1 = multiprocessing.Process(target=pc, args=[1])

# prc1.start()

###############################################################################################
###############################################################################################
###############################################################################################

# import multiprocessing

# def pc(name):
#     print( f"{name} process started")
#     print( f"{name} process ended")

# if __name__ == "__main__":
#     ctx = multiprocessing.get_context('forkserver')

#     prc1 = ctx.Process(target=pc, args=[1])

#     prc1.start()

###############################################################################################
###############################################################################################
###############################################################################################

# example with reental lock
# example with semaphore

# import multiprocessing 

# print( multiprocessing.Lock )
# print( multiprocessing.RLock )
# print( multiprocessing.Condition )
# print( multiprocessing.Semaphore )
# print( multiprocessing.Event )
# print( multiprocessing.Barrier )

###############################################################################################
###############################################################################################
###############################################################################################

# from multiprocessing import Process, Value, Array

# class MyClass():
#     def __init__(self):
#         self.x = 'o'

# obj = MyClass()
# val = Value('u', 'o')
# arr = Array('u', ['o', 'o', 'o'])


# def modifySharedData(o, v, a):
#         print( o.x )
#         print( v.value )
#         print( a[0] )

#         o.x = 'N'           # locally modified only
#         v.value = 'N'
#         a[1] = 'N'

# p1 = Process(target=modifySharedData, args=[obj, val, arr])

# p1.start()
# p1.join()

# print( obj.x )
# print( val.value )
# print( arr[1] )

###############################################################################################
###############################################################################################
###############################################################################################

# from multiprocessing import Process, Manager
# import time

# manager = Manager()

# managerList = manager.list([1])
# orgList = [1]


# def modify(managerList, orgList):
#     managerList[0] = 11
#     orgList[0] = 11

# def show(managerList, orgList):
#     print( managerList )
#     print( orgList )

# modProcess = Process(target=modify, args=[managerList, orgList])
# modProcess.start()
# modProcess.join()

# showProcess = Process(target=show, args=[managerList, orgList])
# showProcess.start()
# showProcess.join()

# print( managerList )
# print( orgList )


# time.sleep(5)

# manager.shutdown()                # after this all the manager's data is destroyed!

# print( 'manager stopped!')
# time.sleep(5)


###############################################################################################
###############################################################################################
###############################################################################################
# from multiprocessing import Process, Manager
# import time

# manager = Manager()
# manager.shutdown()

###############################################################################################
###############################################################################################
###############################################################################################

# import multiprocessing

# q = multiprocessing.Queue()

# def process(queue):
#     while not queue.empty():
#         print( queue.get() )

# pr = multiprocessing.Process(target=process, args=(q, ))

# q.put([1, 2, 3])
# q.put({"key":"val", 21:22})

# pr.start()

###############################################################################################
###############################################################################################
###############################################################################################

# import multiprocessing

# conn1, conn2 = multiprocessing.Pipe()

# print( conn1 )


###############################################################################################
###############################################################################################
###############################################################################################

###############################################################
###############################################################
###############################################################

# import multiprocessing

# c1, c2 = multiprocessing.Pipe()
# c1.send({"key":"val"})
# c1.send([1, 2, 3])


# def task(ch):
#     while ch.poll():
#         print( ch.recv() )

#     ch.close()

# multiprocessing.Process(target=task, args=(c2, )).start()


###############################################################
###############################################################
###############################################################

# import multiprocessing
# import time

# c1, c2 = multiprocessing.Pipe()
# c3, c4 = multiprocessing.Pipe()

# def resend(ch_in, ch_out):
#     while ch_in.poll(5):
#         ch_out.send(ch_in.recv())

# def getPipedData(ch):
#     while ch.poll(5):
#         print( ch.recv() )

# multiprocessing.Process(target=resend, args=[c2, c3]).start()
# multiprocessing.Process(target=getPipedData, args=[c4]).start()

# time.sleep(2.5)
# c1.send('some data')
# c1.send(4-5j)
# c1.send({1})

###############################################################
###############################################################
###############################################################

# import multiprocessing

# c1, c2 = multiprocessing.Pipe()

# c1.send_bytes(b"test bytes")
# c1.send_bytes(b"anoher test bytes")

# def getPipedData(ch):
#     b = bytearray(50)
#     prevMsgLen = 0

#     while ch.poll():
#         prevMsgLen = ch.recv_bytes_into(b, prevMsgLen)

#     print( b )

# multiprocessing.Process(target=getPipedData, args=[c2]).start()

###############################################################
###############################################################
###############################################################

# import queue
# import threading

# q = queue.Queue()

# def task(q):
#     while not q.empty():
#         print( q.get() )

# th1 = threading.Thread(target=task, args=[q])

# q.put({"key":"val"})
# q.put([1, 2])
# q.put({1, 2})

# th1.start()

###############################################################
###############################################################
###############################################################

# import queue

# q = queue.Queue(maxsize=2)   # queue with 2 slots

# q.put('test')
# q.put('test')
# q.put('test')                # block further execution untill a slots frees up in the queue 

###############################################################
###############################################################
###############################################################

# import queue

# q = queue.Queue()

# q.put('someItem')
# q.put({1, 2})
# q.put({"key":"val"})
# q.put(object())

# while not q.empty():
#     print( q.get() )

###############################################################
###############################################################
###############################################################

# import queue

# q = queue.Queue(maxsize=2)

# q.put_nowait('test')
# q.put_nowait('test')
# q.put_nowait('test')      # raises a Full error

###############################################################
###############################################################
###############################################################

# import queue

# q = queue.Queue()

# for i in range(1000):
#     q.put('test')

# while not q.empty():
#     print( q.get() )

###############################################################
###############################################################
###############################################################

# import queue

# q = queue.Queue()

# for i in range(10):
#     q.put('some item')

# for i in range(10):
#     # q.get()           # not neccessary to call
#     q.all_tasks_done()

# q.join()

###############################################################
###############################################################
###############################################################
# <p> - <mark>Queue</mark> and <mark>SimpleQueue</mark> </p>

# import queue

# q1 = queue.Queue()
# q2 = queue.SimpleQueue()      # same as queue but more simple

# q1.put('it 1')
# q1.put('it 2')
# q1.put('it 3')

# q2.put('it 1')
# q2.put('it 2')
# q2.put('it 3')

# for i in range(10):
#     print( q1.get() )         # "it 1"  |  "it 2"  |  "it 3"
#     print( q2.get() )         # "it 1"  |  "it 2"  |  "it 3"


###############################################################
###############################################################
###############################################################
# <p> - <mark>LifoQueue</mark> (stack) </p>

# import queue

# q = queue.LifoQueue()

# q.put('it 1')
# q.put('it 2')
# q.put('it 3')

# for i in range(10):
#     print( q.get() )         # "it 3"  |  "it 2"  |  "it 1"

###############################################################
###############################################################
###############################################################
# <p> - <mark>PriorityQueue</mark> (stack) </p>

# import queue

# q = queue.PriorityQueue()

# q.put('x')
# q.put('a')
# q.put('ka')

# for i in range(10):
#     print( q.get() )         # "a"  |  "ka"  |  "x"   # item with the lowest value retrieved frist from the queue 
