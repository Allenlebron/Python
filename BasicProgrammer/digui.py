def f(n, x):
    if n <= x:
        print(n)
        f(n + 1, x)

f(1,5)