n = int((input()))
a = list(range(0, 10))

result = ''

for x in reversed(a):
    wari = 2 ** x
    result += str(int((n / wari) % 2))

print(result)
