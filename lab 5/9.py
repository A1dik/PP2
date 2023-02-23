import re

string = input("Enter a string: ")
pattern = r'[A-Z][a-z]*'

new_string = re.sub(pattern, lambda match: ' ' + match.group(0), string)

print(new_string)
