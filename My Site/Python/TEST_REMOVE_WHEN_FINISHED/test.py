import datetime
import time
import os

# ts = time.time()

# os.environ['TZ'] = 'Europe/Budapest'
# time.tzset()

t1 = datetime.time(20, 0, 0)
t2 = datetime.time(20, 0, 1)
t3 = datetime.time(20, 0, 0)

print( t1 > t2)
print( t1 == t3)
