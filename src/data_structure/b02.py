a, b = list(map(int, input().split()))
target = list(range(a, b + 1))

result = 'No'

for _a in target:
    if 100 % _a == 0:
        result = 'Yes'
        break

print(result)
