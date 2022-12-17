# 答えがx以下かを判定し、Yesであればtrue, Noであればfalseを返す
def check(x):
    # xは回答候補になる秒数
    result = 0
    for i in range(0, n):
        # i番目のプリンターが、x秒までに処理できる結果を合計
        result += int(x / a[i])
        # 合計がkを上回っているかチェック
    return result >= k


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

left = 1
right = 1000000000

while left < right:
    middle = int((left + right) / 2)
    answer = check(middle)
    if answer:
        right = middle
    else:
        left = middle + 1

print(left)
