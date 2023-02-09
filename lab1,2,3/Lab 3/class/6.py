numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

prime = list(filter(lambda x: is_prime(x), numbers))

print(f'prime: {prime}')
