def f(first, turn):
    if (first >= 273) and turn == 2:
        return True
    elif (first >= 273) and turn != 2:
        return False
    elif turn > 2:
        return False
    else:
        if turn % 2 == 0:  # Петя
            return (
                f(first + 2, turn + 1)
                or f(first + 5, turn + 1)
                or f(first * 4, turn + 1)
            )
        else:
            return (
                f(first + 2, turn + 1)
                or f(first + 5, turn + 1)
                or f(first * 4, turn + 1)
            )


for S in range(1, 273):
    if f(S, 0):
        print(S)
        break
