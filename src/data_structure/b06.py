n = int(input())
a = list(map(int, input().split()))
q = int(input())
target = []

for x in range(0, q):
    target.append(list(map(int, input().split())))

# 累積和の計算
s = [[0, 0]]

for i in range(1, n + 1):
    if a[i - 1] == 1:
        s.append([s[i - 1][0] + 1, s[i - 1][1]])
    else:
        s.append([s[i - 1][0], s[i - 1][1] + 1])

for _target in target:
    win = s[_target[1]][0] - s[_target[0] - 1][0]
    lose = s[_target[1]][1] - s[_target[0] - 1][1]

    if win > lose:
        print('win')
    elif win == lose:
        print('draw')
    else:
        print('lose')
