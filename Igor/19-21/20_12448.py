def f(first, second, turn):
    if first * second >= 777:
        if turn == 3:
            return True
        else:
            return False
    if turn > 3:
        return False
    else:
        if turn % 2 == 0:  # Peta
            return (
                f(first + 3, second, turn + 1)
                or f(first, second * 2, turn + 1)
                or f(first * 2, second, turn + 1)
                or f(first, second + 3, turn + 1)
            )
        else:  # vana 53 54 55
            return (
                f(first + 3, second, turn + 1)
                and f(first, second * 2, turn + 1)
                and f(first * 2, second, turn + 1)
                and f(first, second + 3, turn + 1)
            )


for S in range(1, 111):
    if f(7, S, 0):
        print(S)