n = int((input()))
a = list(map(int, input().split()))

result = 'No'

for a1 in a:
    for a2 in a:
        for a3 in a:
            if a1 == a2 or a2 == a3 or a1 == a3:
                continue
            if a1 + a2 + a3 == 1000:
                result = 'Yes'

print(result)
