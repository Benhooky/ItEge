def f(first, second, turn):
    if first + second >= 79:
        if turn == 2:
            return True
        else:
            return False
    if turn > 2:
        return False
    else:
        if turn % 2 == 0 :  # Peta
            return (
                f(first + 1, second, turn + 1)
                or f(first, second * 3, turn + 1)
                or f(first * 3, second, turn + 1)
                or f(first, second + 1, turn + 1)
            )
        else:  # vana
            return (
                f(first + 1, second, turn + 1)
                or f(first, second * 3, turn + 1)
                or f(first * 3, second, turn + 1)
                or f(first, second + 1, turn + 1)
            )
for S in range(1, 73):
    if f(6, S, 0):
        print(S)
        break