# A time object represents a (local) time of day, indepen#dent of any particular day, and subject to adjustment via a tzinfo object.
import datetime

# naive time objects
t = datetime.time(hour=8,minute=30,second=15,microsecond=10)
print(type(t))
print(t)

print(t.hour)
print(t.second)
print(t.tzinfo)
