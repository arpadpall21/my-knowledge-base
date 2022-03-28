import module1 

print( module1.a )
print( module1.b )

def importModule():
    import module2

    print( module2.x )
    print( module2.y )

importModule()