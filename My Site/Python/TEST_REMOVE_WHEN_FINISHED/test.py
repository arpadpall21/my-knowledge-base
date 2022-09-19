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

# import random

# print( random.random() )        # if no seep specified the current system time is used as start seed value

# random.seed(2.5)                # seeding random generation start value (further random generation will be deterministic)    
# print( random.random() )        # 0.41877545666909954  


# st = random.getstate()          # gets the current start value
# random.setstate(st)             # setting a previously capture state (further random generation will be deterministic by using thi start value)

# print( random.random() )        # 0.9404475600150654   

###############################################################################################
###############################################################################################

import random

random.seed(1)                        # deterministic random generation (start value set)

print( random.randbytes(10) )         # b'\xf5\xb1e"JX\xb7\x91\xf1\xd8'   # random 10 byte sequence

print( random.randrange(10) )         # 1     # random number picked from the range
print( random.randrange(0, 10, 2) )   # 4     # random number picked from the range (step restricted)

print( random.randint(0, 2) )         # 0     # random number picked from the range