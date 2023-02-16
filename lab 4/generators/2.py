n = int(input("Enter a number: "))

def even_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(*even_gen(n), sep=", ")