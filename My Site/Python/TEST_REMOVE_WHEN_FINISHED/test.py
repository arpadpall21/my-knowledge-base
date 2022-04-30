class Ctx:
    def __enter__(self):
        pass
    
    def __exit__(self, errTyp, errMsg, errTb):
        return True

ctxObj = Ctx()

with ctxObj as val:
    raise Exception('some exception')
    
print( 'after with' )
