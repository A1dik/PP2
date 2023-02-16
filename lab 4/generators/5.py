n = int(input("Enter a number: "))

def countdown(n):
    while n >= 0:
        yield n
        n -= 1
print(*countdown(n))