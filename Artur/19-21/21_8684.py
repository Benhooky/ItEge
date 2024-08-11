def f(first, second, turn):
    if first + second >= 175:
        if turn == 2 or turn == 4:
            return True
        else:
            return False
    if turn > 4:
        return False
    if turn % 2 == 0:
        return f(first + 1, second, turn + 1) and f(first, second + 1, turn + 1) and f(first * 3, second, turn + 1) and f(first, second * 3, turn + 1)
    else:
        return f(first + 1, second, turn + 1) or f(first, second + 1, turn + 1) or f(first * 3, second, turn + 1) or f(first, second * 3, turn + 1)

for S in range(1, 155):
    if f(19, S, 0):
        print(S)