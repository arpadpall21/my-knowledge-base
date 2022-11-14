def my_decorator(fn):
    res1 = fn()
    res2 = fn()



    return res1 + ' ' + res2

@my_decorator
def test():
    return 'test'

print( 
    test()
)

