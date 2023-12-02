def f(first, second, turn):
    if first + second >= 91:
        if turn == 3:
            return True
        else:
            return False
    if turn > 3:
        return False
    else:
        if turn % 2 == 0:  # Peta
            return (
                f(first + 1, second, turn + 1)
                or f(first, second * 4, turn + 1)
                or f(first * 4, second, turn + 1)
                or f(first, second + 1, turn + 1)
            )
        else:  # vana
            return (
                f(first + 1, second, turn + 1)
                and f(first, second * 4, turn + 1)
                and f(first * 4, second, turn + 1)
                and f(first, second + 1, turn + 1)
            )


for S in range(1, 85):
    if f(5, S, 0):
        print(S)