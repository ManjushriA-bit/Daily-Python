import calendar

yy = 2025
mm = 3

cal = calendar.month(yy, mm)

for line in cal.split("\n"):
    print(line.center(60))
