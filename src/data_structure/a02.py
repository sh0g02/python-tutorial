n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

result = 'No'

for _a in a:
    if _a == x:
        result = 'Yes'
        break

print(result)
