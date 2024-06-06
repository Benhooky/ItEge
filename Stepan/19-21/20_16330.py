def F(first, second, turn):
    if first + second >= 59:#игра кончилась
        if turn == 3:#Выиграл Петя вторым ходом
            return True
        else:
            return False
    if turn > 3:
        return False
    if turn %2 == 0:#Петя
        return F(first + 1, second, turn + 1) or F(first, second + 1, turn + 1) or F(first * 2, second, turn + 1) or F(first, second * 2, turn + 1)
    else:#Ваня
        return F(first + 1, second, turn + 1) and F(first, second + 1, turn + 1) and F(first * 2, second, turn + 1) and F(first, second * 2, turn + 1)
    
for S in range(1,54):
    if F(5,S,0):
        print(S)