def f(first, turn):
    if first >= 58:
        if turn == 3:
            return True
        else: 
            return False
    if turn > 3:
        return False
    if turn % 2 == 0:
        return f(first + 1, turn + 1) or f(first + 4, turn + 1) or f(first * 2, turn + 1) # петя
    else:
        return f(first + 1, turn + 1) and f(first + 4, turn + 1) and f(first * 2, turn + 1) # ваня

for S in range(1, 58):
    if f(S, 0):
        print(S)