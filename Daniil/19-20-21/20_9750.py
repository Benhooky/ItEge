def f (first,turn):
    if first>=88:#игра закончилась
        if turn == 3:#Петя победил 2 ходом
            return True
        else:
            return False
    if turn>3:#перебор ходов
        return False
    if turn%2==0:#Ходит Петя
        return f(first+1,turn+1) or f(first+4,turn+1) or f(first*3,turn+1)
    else:#Ходит Ваня
        return f(first+1,turn+1) and f(first+4,turn+1) and f(first*3,turn+1)
    
for S in range(1,88):
    if f(S,0):
        print(S)