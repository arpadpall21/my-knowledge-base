# import threading
# import time

# USE_DAEMON = False

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

# def th(name):
#     print(f'{name} started')
#     countrange(name, r)
#     print(f'{name} end!')


# a = threading.Thread(target=th, args=["Thread-1"], daemon=USE_DAEMON)
# b = threading.Thread(target=th, args=["Thread-2"], daemon=USE_DAEMON)
# c = threading.Thread(target=th, args=["Thread-2"], daemon=USE_DAEMON)
# d = threading.Thread(target=th, args=["Thread-2"], daemon=USE_DAEMON)

# a.start()
# b.start()
# c.start()
# d.start()

# a.join()
# b.join()
# c.join()
# d.join()

# # countrange("Main", r)



# print( f"Running time: {time.time() - start}" )



###############################################################################################
###############################################################################################
###############################################################################################

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

import threading

lock = threading.Lock()
lock.acquire()

print( lock.locked() )

lock.release()
print( lock.locked() )