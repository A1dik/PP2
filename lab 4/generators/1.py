def square_gen(N):
    for i in range(N):
        yield i**2
n = int(input("Enter a number: "))
sq = square_gen(n)
print(*sq)
