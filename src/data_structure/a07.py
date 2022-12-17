d = int(input())
n = int(input())
start = [0] * 100009
end = [0] * 100009
day_before_ratio_list = [0] * 100009

for i in range(1, n + 1):
    start[i], end[i] = list(map(int, input().split()))

# 前日比を求める
for i in range(1, n + 1):
    day_before_ratio_list[start[i]] += 1
    day_before_ratio_list[end[i] + 1] -= 1

# 累積和を取る
answer = [0] * 100009

for _d in range(1, d + 1):
    answer[_d] = answer[_d - 1] + day_before_ratio_list[_d]

for _d in range(1, d + 1):
    print(answer[_d])
