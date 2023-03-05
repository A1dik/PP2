string = "Hello World"

bolsh_count = sum(1 for char in string if char.isupper())
men_count = sum(1 for char in string if char.islower())

print(bolsh_count)
print(men_count)
