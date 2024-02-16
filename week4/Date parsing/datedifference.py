import datetime

x = datetime.datetime(2024, 2, 1)
y = datetime.datetime(2024, 1, 31)
difference = x - y
seconds = difference.total_seconds()

print(seconds)