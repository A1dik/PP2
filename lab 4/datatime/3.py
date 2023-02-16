from datetime import datetime

current_date = datetime.now()
truncated_date = current_date.replace(microsecond=0)
print("Datetime after dropping microseconds: ", truncated_date)