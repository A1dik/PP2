a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))

def squares(a, b):
    for i in range(a, b+1):
        yield i**2
sq = squares(a,b)
print(*sq)


