import time
import math

number = 25100
milliseconds = 2123

time.sleep(milliseconds/1000)
result = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
