import datetime

date1 = datetime.datetime(2024, 2, 15, 10, 20, 30)
date2 = datetime.datetime(2024, 2, 19, 12, 34, 56)
time_delta = date2 - date1
seconds = time_delta.total_seconds()
print("Difference between two dates in seconds:", int(seconds))
