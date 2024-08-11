def f(first, second, turn):
    if first * second >= 455:
        if turn == 2:
            return True
        else:
            return False
    if turn > 2:
        return False
    if turn % 2 == 0:
        return f(first + 1, second, turn + 1) or f(first, second + 1, turn + 1) or f(first * 2, second, turn + 1) or f(first, second * 2, turn + 1)
    else:
        return f(first + 1, second, turn + 1) or f(first, second + 1, turn + 1) or f(first * 2, second, turn + 1) or f(first, second * 2, turn + 1)

for S in range(1, 91):
    if f(5, S, 0):
        print(S)