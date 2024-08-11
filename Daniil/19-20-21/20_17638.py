def f(first,second,turn):
    if first+second >= 65: #Игра закончилась
        if turn == 3: #Выиграл Петя втором ходом
            return True
        else:
            return False
    if turn > 3:
        return False
    if turn % 2 == 0:#Сейчас будет ходить Петя
        return f(first+1,second,turn+1) or f(first,second + 1, turn+1) or f(first*3,second,turn+1) or f(first,second*3,turn+1)
    else:#Сейчас будет ходить Ваня
        return f(first+1,second,turn+1) and f(first,second + 1, turn+1) and f(first*3,second,turn+1) and f(first,second*3,turn+1)

for S in range(1,59):
    if f(6, S, 0):
        print(S)