import re

string = input("Enter a string: ")
pattern = r'[a-z]+(_[a-z]+)*'

matches = re.findall(pattern, string)

for match in matches:
    print(match)
