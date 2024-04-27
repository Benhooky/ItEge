def f(first,second,turn):
    if first * second > 384:#если верно - игра кончилась
        if turn == 2 or turn == 4:# игра кончилась в пользу Пети первым ходом
            return True
        else:# игра кончилась каким-то другим образом
            return False
    elif turn > 4:# игра не закончилась на первом ходе Пети, значит это не то, что нужно
        return False
    else:#игра продолжается
        if turn%2==0:# ходит Петя
            return f(first+5,second,turn+1) and f(first,second+5,turn+1) and f(first*2,second,turn+1) and f(first,second*2,turn+1)
        else:# ходит Ваня
            return f(first+5,second,turn+1) or f(first,second+5,turn+1) or f(first*2,second,turn+1) or f(first,second*2,turn+1)
# победитель = всегда or
# проигрваший = and, если поддался (неудачный) = or 
for S in range(1,55):
    if f(8,S,0):
        print(S)