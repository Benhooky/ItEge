def f(n, x):
    if x == 15:
        return {n}
    return f(n + 10, k+1) and f(n-5, k+1)
print(len(f(1, 0)))