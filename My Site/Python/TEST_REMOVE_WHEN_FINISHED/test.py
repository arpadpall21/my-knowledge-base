import datetime
import time
import os

# os.environ['TZ'] = 'Europe/Budapest'
# time.tzset()

class Timezone(datetime.tzinfo):
    pass

myTz = Timezone()

today = datetime.datetime.today()
now = datetime.datetime.now(tz=myTz)
utcnow = datetime.datetime.utcnow()

print( today )
print( now )
print( utcnow )