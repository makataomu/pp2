import datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
