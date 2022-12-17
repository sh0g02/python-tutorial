def search(target):
    left = 1
    right = n

    while left <= right:
        # 真ん中をとる
        middle = int((left + right) / 2)
        if target < a[middle]:
            # ターゲットが真ん中よりも小さい場合
            # 真ん中より右側を対象から外す
            right = middle - 1
        if target == a[middle]:
            return middle
        if target > a[middle]:
            # 真ん中より左側を対象から外す
            left = middle + 1
    return -1


n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

answer = search(x)
print(answer + 1)
