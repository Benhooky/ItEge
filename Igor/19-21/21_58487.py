def f(first, second, turn):
    if first >= 48 or second >= 48:
        if turn == 4:
            return True
        else:
            return False
    if turn > 4:
        return False
    if turn % 2 == 0:  # петя
        if first > second:
            return (
                f(first + 1, second, turn + 1)
                and f(first + 2, second, turn + 1)
                and f(first + 3, second, turn + 1)
                and f(first, second * 2, turn + 1)
            )
        elif first < second:
            return (
                f(first * 2, second, turn + 1)
                and f(first, second + 1, turn + 1)
                and f(first, second + 2, turn + 1)
                and f(first, second + 3, turn + 1)
            )
        else:
            return (
                f(first + 1, second, turn + 1)
                and f(first + 2, second, turn + 1)
                and f(first + 3, second, turn + 1)
                and f(first, second + 1, turn + 1)
                and f(first, second + 2, turn + 1)
                and f(first, second + 3, turn + 1)
            )
    else:  # vana
        if first > second:
            return (
                f(first + 1, second, turn + 1)
                or f(first + 2, second, turn + 1)
                or f(first + 3, second, turn + 1)
                or f(first, second * 2, turn + 1)
            )
        elif first < second:
            return (
                f(first * 2, second, turn + 1)
                or f(first, second + 1, turn + 1)
                or f(first, second + 2, turn + 1)
                or f(first, second + 3, turn + 1)
            )
        else:
            return (
                f(first + 1, second, turn + 1)
                or f(first + 2, second, turn + 1)
                or f(first + 3, second, turn + 1)
                or f(first, second + 1, turn + 1)
                or f(first, second + 2, turn + 1)
                or f(first, second + 3, turn + 1)
            )


for S in range(1, 47):
    if f(39,S,0):
        print(S)
