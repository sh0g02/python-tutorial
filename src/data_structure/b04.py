n = list(input())
size = len(n)

result = 0

for i, x in enumerate(n):
    if x == '1':
        result += 2 ** (size - 1 - i)

print(result)
