n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
target = []

for x in range(0, q):
    target.append(list(map(int, input().split())))

# 累積和の計算
s = [0]

for x in range(1, n + 1):
    s.append(s[x - 1] + a[x - 1])

for _target in target:
    print(s[_target[1]] - s[_target[0] - 1])
