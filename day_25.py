import math

def is_prime(number):
    if number <= 1:
        return "Not prime"
    if number == 2:
        return "Prime"
    if number % 2 == 0:
        return "Not prime"

    max_divisor = math.isqrt(number) + 1
    for i in range(3, max_divisor, 2):
        if number % i == 0:
            return "Not prime"

    return "Prime"

n = int(input())
for _ in range(n):
    number = int(input())
    result = is_prime(number)
    print(result)
