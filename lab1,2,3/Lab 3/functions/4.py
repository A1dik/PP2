def filter_pr(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return list(filter(is_prime, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_pr(numbers)

print("Prime numbers:", prime_numbers)
