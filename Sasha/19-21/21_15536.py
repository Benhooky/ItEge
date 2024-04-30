def f(first,second,turn):
    if first+second>=123:#игра закончилась
        if turn == 4 or turn == 2:
            return True
        else:
            return False
    if turn>4:#перебор ходов не интересен
        return False
    else:
        if turn%2==0:#Петя
            return f(first+1,second,turn+1) and f(first*2,second,turn+1) and f(first,second+1,turn+1) and f(first,second*2,turn+1)
        else:#Ваня
            return f(first+1,second,turn+1) or f(first*2,second,turn+1) or f(first,second+1,turn+1) or f(first,second*2,turn+1)
for S in range(1,110):
    if f(13,S,0):
        print(S)