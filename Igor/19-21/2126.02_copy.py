def f(first,turn):
    if first <= 116:
        if turn == 2 or turn == 4:
            return True
        else:
            return False
    if turn > 4:
        return False
    else:
        if turn % 2 == 0:  # Peta
            return (
                f(first - 7 ,turn + 1)
                and f(first // 3, turn + 1)
            )
        else:  # vana
            return (
                f(first - 7, turn + 1)
                or f(first//3, turn + 1)
            )


for S in range(117,10000):
    if f(S, 0):
        print(S)
