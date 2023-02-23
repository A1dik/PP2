import re

string = input("Enter a string: ")
pattern = r'[ ,.]'

new_string = re.sub(pattern, ':', string)

print(new_string)
