def f(from1,to1,lastUsedCommand):
    if from1 > to1+1:
        return 0
    if from1 == to1:
        return 1
    else:
        if lastUsedCommand == 'A':
            return f(from1*2,to1,'B')+f(from1*3,to1,'C')
        else:
            return f(from1-1,to1,'A')+f(from1*2,to1,'B')+f(from1*3,to1,'C')
print(f(3,15,'X'))