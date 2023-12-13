def F(first: int, second: int, turn: int):
    if first + second >= 67:
        if turn == 2:
            return True
        else:
            return False
    if turn > 2:
        return False
    else:
        if turn % 2 == 0:  # петя
            return (
                F(first + 1, second, turn + 1)
                or F(first, second + 1, turn + 1)
                or F(first + second, second, turn + 1)
                or F(first, second + first, turn + 1)
            )
        else:
            return (
                F(first + 1, second, turn + 1)
                or F(first, second + 1, turn + 1)
                or F(first + second, second, turn + 1)
                or F(first, second + first, turn + 1)
            )
