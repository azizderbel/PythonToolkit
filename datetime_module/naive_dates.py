# naive dates object do not include timezone information
import datetime


# create a date object
"""d = datetime.date(2017,6,1)
print(type(d))                # <class 'datetime.date'>
print(d)                      # 2017-06-01


d = datetime.date.today()
print(type(d))                # <class 'datetime.date'>
print(d)


d = datetime.date.fromisoformat("2041-01-04")
print(type(d))                # <class 'datetime.date'>
print(d)
"""

d = datetime.date.fromtimestamp(1687727188)
print(type(d))                # <class 'datetime.date'>
print(d)


print(d.day)
print(d.month)
print(d.year)

print(d.timetuple())
print(d.isoformat())
print(d.strftime("%A : the %dth of %B %Y %H:%M:%S"))