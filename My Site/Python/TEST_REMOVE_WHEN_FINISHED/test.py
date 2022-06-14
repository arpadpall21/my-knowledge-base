from abc import ABC, abstractclassmethod

class AbcCls(ABC):
    @abstractclassmethod
    def baseMethod(self):
        return 'base value'


class TestClass(AbcCls):
    def baseMethod(self):
        return super().baseMethod()
        
inst = TestClass()
print( inst.baseMethod() )
