def f(first, second, turn):
    if first + second >= 375:
        if turn == 4 or turn == 2:
            return True
        else:
            return False
    elif turn > 4:
        return False
    else:
        if turn % 2 == 0:
            return (
                f(first + 3, second, turn + 1)
                and f(first * 2, second, turn + 1)
                and f(first, second + 3, turn + 1)
                and f(first, second * 2, turn + 1)
            )
        else:
            return (
                f(first + 3, second, turn + 1)
                or f(first * 2, second, turn + 1)
                or f(first, second + 3, turn + 1)
                or f(first, second * 2, turn + 1)
            )


for S in range(348):
    if f(27, S, 0):
        print(S)
