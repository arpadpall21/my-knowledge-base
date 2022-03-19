class D:
    pass
    
class C:
    pass
    
class B:
    pass
    
class A(B, C):
    pass
    
obj = A()


print( issubclass(A, B) )
print( issubclass(A, C) )
print( issubclass(C, A) )

print( issubclass(D, (A, B, C)) )


# print( type(obj) )
# print( obj.__class__ )


