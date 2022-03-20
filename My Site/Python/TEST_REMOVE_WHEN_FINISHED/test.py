class TestClass:
    pass
    
def method(self):
    return 22
    
def privMethod(self):
    return 22
    
TestClass.attr = 21
TestClass.method = method

TestClass._TestClass__privAttr = 31
TestClass._TestClass__privMethod = privMethod

obj = TestClass()

print( obj.attr )
print( obj.method() )

print( obj.attr )
print( obj.method() )


