from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday's date: ", yesterday)
print("Today's date: ", today)
print("Tomorrow's date: ", tomorrow)