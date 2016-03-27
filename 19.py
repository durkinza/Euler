import datetime as dt
delta = dt.timedelta(days=1)

dow = 6
day = 1
sdate = dt.datetime(1901, 1, 1)
edate = dt.datetime(2000, 12, 31)

c = 0
while sdate <= edate:
    if (sdate.day == day) and (sdate.weekday() == dow):
        c = c + 1
    sdate = sdate + delta

print c
