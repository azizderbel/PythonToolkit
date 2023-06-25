import datetime
import pytz

'''dt1 = datetime.datetime.today()
dt2 = datetime.datetime.now()
dt3 = datetime.datetime.utcnow()

print(dt1)
print(dt2)
print(dt3)

print(dt1.tzinfo)
print(dt2.tzinfo)
print(dt3.tzinfo)'''


dt = datetime.datetime(2006,5,26,12,12,30,45, tzinfo=pytz.UTC)
print(dt)
print(dt.tzinfo)


dt2 = datetime.datetime.now(tz=pytz.UTC)
print(dt2)



for tz in pytz.all_timezones:
    print(tz)

dt3 = dt2.astimezone(tz=pytz.timezone('US/Samoa'))
print(dt3)