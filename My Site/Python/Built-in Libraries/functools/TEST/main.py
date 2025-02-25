import functools

####################################################################
### cache ###
####################################################################
# @functools.cache
# def add(a, b):
#     return a + b

# add(1, 2)
# add(1, 3)

# add(1, 2)           # function not called but looks up the cache resutl
# add(1, 3)           # function not called but looks up the cache resutl

# print(add.cache_info())       # -> CacheInfo(hits=2, misses=2, maxsize=None, currsize=2)
# add.cache_clear()             # clears the cache
# print(add.cache_info())       # -> CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)
# print(add.cache_parameters())       # -> {'maxsize': None, 'typed': False}



####################################################################
### lru_cache ###
####################################################################
# @functools.lru_cache(maxsize=64)
# def add(a, b):
#     return a + b

# add(1, 2)
# add(1, 3)

# add(1, 2)           # function not called but looks up the cache resutl
# add(1, 3)           # function not called but looks up the cache resutl

# print(add.cache_info())       # -> CacheInfo(hits=2, misses=2, maxsize=None, currsize=2)
# add.cache_clear()             # clears the cache
# print(add.cache_info())       # -> CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)
# print(add.cache_parameters())       # -> {'maxsize': None, 'typed': False}


# def subtract(a, b):
#     print('----')
#     return a - b

# cached_subtract = functools.lru_cache()(subtract)

# print(cached_subtract(2, 1))
# print(cached_subtract(3, 1))

# print(cached_subtract(2, 1))
# print(cached_subtract(3, 1))




####################################################################
### reduce ###
####################################################################

# print( functools.reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]) )       # -> 15
# print( functools.reduce(lambda a, b: a + b, [1, 2, 3, 4, 5], 10) )       # -> 25  # starts with 10



####################################################################
### singledispatch ###
####################################################################
# @functools.singledispatch
# def process(value):
#     raise NotImplementedError("Unsupported type")


# @process.register
# def _(value: int):
#     return f"Processing an integer: {value}"


# @process.register
# def _(value: str):
#     return f"Processing a string: {value}"


# @process.register
# def _(value: list):
#     return f"Processing a list of length {len(value)}"

# # Usage
# print(process(10))          # Output: Processing an integer: 10
# print(process("hello"))     # Output: Processing a string: hello
# print(process([1, 2, 3]))   # Output: Processing a list of length 3


