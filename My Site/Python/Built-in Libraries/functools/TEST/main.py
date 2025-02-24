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
### @cached_property ###
####################################################################
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + " " + self.surname

    @functools.cached_property                      # cached property
    def full_name_flipped(self):
        print('------------')
        return self.surname + " " + self.name


peti = Person('Peter', 'Pall')

# print( peti.full_name )               # -> Peter Pall (regular @property decorator)
# peti.full_name = "Peter Bela"         # AttributeError (because no setter attirubte configured)
# del peti.full_name                    # AttributeError (because no deleter attirubte configured)


print( peti.full_name_flipped )       # -> Pall Peter 
print( peti.full_name_flipped )       # -> Pall Peter (cached attribute is not recomputed )

peti.full_name_flipped = "Pall Bela"
print( peti.full_name_flipped )
