def check(x):
    # xは回答候補
    result = (x ** 3 + x)
    return result >= n


n = int(input())

left = 1
right = 100
# 1≤N≤100000なので、条件（x ** 3 + x）から上限として100あれば十分

while right - left > 0.001:
    # 継続条件誤差0.001を切ったらあとの計算不要
    middle = (left + right) / 2
    answer = check(middle)
    if answer:
        right = middle
    else:
        left = middle + 0.001

print(left)
