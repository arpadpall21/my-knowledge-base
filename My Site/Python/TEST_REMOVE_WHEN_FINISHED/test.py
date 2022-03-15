class BaseClass1:
    def __init__(self):
        self.p1 = 21
    
    def someMethod():
        return 'someMethod-val'
    
class BaseClass2:
    def __init__(self):
        self.p2 = 22
    
class TestClass(BaseClass1):
    def __init__(self):
        # super()
        self.p3 = 23
    
    
myObj = TestClass()
print( myObj.p3 )