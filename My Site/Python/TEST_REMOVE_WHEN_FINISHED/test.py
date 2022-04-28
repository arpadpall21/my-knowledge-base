from contextlib import contextmanager

@contextmanager
def ctxmanager():
    print('setup---------')
    yield "Hello World!"
    print('teardown------')
    return True

with ctxmanager() as alias:
    print('ctx manger context ->')
    print( alias )
    raise Exception('my exception')

print( '---------------------------after with')