def f(a, b, LastUsedCommand):
    if a > b:
        return 0
    if a == b:
        if LastUsedCommand != 'B':
            return 1
        else:
            return 0
    else:
        return f(a + 2, b, 'A') + f(a + 3, b, 'B') + f(a * 2, b, 'C')
print(f(3, 20, 'D'))