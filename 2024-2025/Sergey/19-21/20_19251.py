def f(first, turn):
    if first >= 132:
        if turn == 3:
            return True
        else:
            return False
    if turn > 4:
        return False
    if turn % 2 != 0: # Ваня
        return f(first + 3, turn + 1) and f(first+6, turn + 1) and f(first*3, turn + 1)
    else: #Петя
        return f(first + 3, turn + 1) or f(first+6, turn + 1) or f(first*3, turn + 1)
    
for S in range(1, 132):
    if f(S, 0):
        print(S)