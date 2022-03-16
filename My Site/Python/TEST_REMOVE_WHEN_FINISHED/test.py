class BaseClass:
    def __init__(self, a):
        self.a = a
    
    baseProp = 100
    
    def baseMethod(cls):
        return 201

class TestClass(BaseClass):
    def __init__(self, a, b):
        super(self, a)
        self.b = b
    
    
myObj = TestClass('a', 'b')


print( myObj.__dict__ )
