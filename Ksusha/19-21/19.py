def F(first, second, turn):
    if (first + second >= 342) and turn == 2:
        return True
    elif (first + second >= 342) and turn != 2:
        return False
    elif turn > 2:
        return False
    else:
        if turn % 2 == 0:
            return (
                F(first * 5, second, turn + 1)
                or F(first, second * 5, turn + 1)
                or F(first + 2, second, turn + 1)
                or F(first, second + 2, turn + 1)
            )
        else:
            return (
                F(first * 5, second, turn + 1)
                or F(first, second * 5, turn + 1)
                or F(first + 2, second, turn + 1)
                or F(first, second + 2, turn + 1)
            )


for S in range(1, 326):
    if F(11, S, 0):
        print(S)
        break
