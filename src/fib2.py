def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    # 1つの値を返しつつ関数から復帰
    # 式を引数に持たないreturnはNoneを返す
    # 関数の末尾に達した場合もNoneを返す
    return result


f100 = fib2(100)

print(f100)
