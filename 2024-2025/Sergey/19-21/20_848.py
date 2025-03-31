def f(first,turn):
    if first>=51:
        if turn==3:
            return True
        else:
            return False
    if turn>4:
        return False
    if turn%2==0:#Петя
        if first%2==0:
            return f(first+1,turn+1) or f(first+3,turn+1) 
        else:
            return f(first*3,turn+1)
    else:#Ваня
        if first%2==0:
            return f(first+1,turn+1) and f(first+3,turn+1) 
        else:
            return f(first*3,turn+1)
for S in range(1,51):
    if f(S,0):
        print(S)