# timedelats  represents a duration, the difference between two dates or times
import datetime


td1 = datetime.timedelta(
    days=1,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    weeks=1
)
print(type(td1))
print(td1) # 8 days, 0:00:00


td2 = datetime.timedelta(
    weeks=3
)
print(type(td2))
print(td2) # 21 days, 0:00:00

print(td1 == td2)    # False
print(td1 < td2)     # True
print(td1 != td2)    # True


td1 = td1 + datetime.timedelta(weeks=2)
print("after addition")
print(td1 < td2)     # True


td3 = datetime.date.today() - datetime.date.fromisoformat("2023-06-25")
print(type(td3))
print(td3)


print(datetime.date.today() + datetime.timedelta(days=55))
# return a new date object