fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

def fah_to_cent(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

cent = fah_to_cent(fahrenheit)

print('our cent is:',cent)
