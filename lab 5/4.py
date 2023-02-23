import re

string = input("Enter a string: ")
pattern = r'[A-Z][a-z]*'

matches = re.findall(pattern, string)

for match in matches:
    print(match)
