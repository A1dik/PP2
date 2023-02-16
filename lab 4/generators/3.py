n = int(input("Enter a number: "))

def div_3_4_gen(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
div = div_3_4_gen(n)
print(*div)