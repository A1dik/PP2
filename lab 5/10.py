import re

string = input("Enter a string in camel case: ")
pattern = r'(?<!^)(?=[A-Z])'

new_string = re.sub(pattern, '_', string).lower()

print(new_string)
