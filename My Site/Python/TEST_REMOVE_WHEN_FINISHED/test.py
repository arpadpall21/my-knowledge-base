class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.end = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.end:
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

iteratorInstance = MyIterator('abc')

iteratorObj = iter(iteratorInstance)

print( next(iteratorObj) )
print( next(iteratorObj) )
print( next(iteratorObj) )
# print( next(iteratorObj) )

for i in iteratorInstance:
    print( i )


