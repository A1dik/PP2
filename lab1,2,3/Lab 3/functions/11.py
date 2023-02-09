def is_palindrome(input_string):
    # Remove any spaces and make all characters lowercase
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]
s='sahadaha'
s2='sahaahas'
print(is_palindrome(s2))