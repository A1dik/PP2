import re

string = input("Enter a string in snake case: ")
pattern = r'_([a-z])'

new_string = re.sub(pattern, lambda match: match.group(1).upper(), string)

print(new_string)
