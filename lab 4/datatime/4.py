from datetime import datetime

date1 = datetime(2020, 4, 15)
date2 = datetime(2023, 4, 15)

difference = abs(date2 - date1).total_seconds()
print("Difference between dates in seconds: ", difference)