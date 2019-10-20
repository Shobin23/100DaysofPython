from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())

#what type of object does this chur out
print(type(datetime.today()))

todaydate = date.today()
print(todaydate)
print(type(todaydate))

print(todaydate.month)

christmas = date(2019,12,25)
print((christmas - todaydate).days)

#Timedelta (gap in time measured out)
t = timedelta(days = 4,hours=10)
print(t.days)
today = datetime.today()

eta = timedelta(hours = 1)
newtime = eta+today
print(newtime)