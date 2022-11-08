def fib(n):
    a, b = 0, 1
    # nまでのフィボナッチ数列を表示する
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
