import datetime

now = datetime.datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print(now_without_microseconds)
