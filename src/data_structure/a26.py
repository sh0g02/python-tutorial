import math


def is_prime(x):
    _x = int(math.sqrt(x))
    for i in range(2, _x + 1):
        if x % i == 0:
            return False
    return True


q = int(input())
x = [0] * 100009

for i in range(1, q + 1):
    x[i] = int(input())

for i in range(1, q + 1):
    answer = is_prime(x[i])
    if answer:
        print('Yes')
    else:
        print('No')
