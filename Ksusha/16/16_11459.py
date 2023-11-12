def F(n):
    if n < 10:
        return n
    else:
        return n % 10 + 8 * F(n // 10)


print(F(10**30))
