from datetime import datetime, time, date

print(datetime.now())
print(datetime(2020, 10, 12, 12, 6, 11, 123456))
#  https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(date(2020, 10, 12).strftime("%Y %B %d."))
print(datetime(2020, 10, 12).isoformat())
print(date(2020, 10, 12) - date(2019, 1, 1))

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

d = date(2023, 1, 1)
t = time(12, 12, 33, 123456)
print(d)
print(t)
print(datetime.combine(d, t))
