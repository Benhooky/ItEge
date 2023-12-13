def f(first, second, turn):
    if first + second <= 20:
        if turn == 2 or turn == 4:
            return True
        else:
            return False
    elif turn > 4:
        return False
    else:
        if turn % 2 == 0:  # peta
            return (
                (f(first, second - 1, turn + 1))
                and (f(first, second // 2, turn + 1))
                and (f(first - 1, second, turn + 1))
                and (f(first // 2, second, turn + 1))
            )
        else:  # vana
            return (
                f(first - 1, second, turn + 1)
                or f(first // 2, second, turn + 1)
                or f(first, second - 1, turn + 1)
                or f(first, second // 2, turn + 1)
            )


for s in range(10, 1000):
    if f(10, s, 0):
        print(s)
