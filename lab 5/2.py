import re

string = input("Enter a string: ")
pattern = r'a[b]{2,3}'

if re.match(pattern, string):
    print("Match found!")
else:
    print("No match found.")
