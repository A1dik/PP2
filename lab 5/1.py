import re

string = input("Enter a string: ")
pattern = r'a[b]*'

if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")
