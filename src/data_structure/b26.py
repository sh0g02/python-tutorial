n = int(input())
d = [False] * (n + 1)

for i in range(2, n + 1):
    if not d[i]:
        for j in range(i * 2, n + 1, i):
            # iの倍数は確実に素数でないので削除
            d[j] = True

for i in range(2, n + 1):
    if not d[i]:
        print(i)
