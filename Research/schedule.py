from datetime import datetime, timedelta

today = datetime.today().date()

print(type(today))
print(today)

threshold = today + timedelta(days=7)
print(threshold)
