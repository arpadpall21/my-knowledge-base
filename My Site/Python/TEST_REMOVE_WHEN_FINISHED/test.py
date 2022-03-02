def genFn():
    yield 'one'
    yield 'two'
    return 'three'

genObj = genFn()

print( next(genObj, 'defVal') )
print( next(genObj, 'defVal') )
print( next(genObj, 'defVal') )