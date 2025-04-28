def f(from1, to1, lastUsedCmd):
    if from1==to1:
        return 1
    elif from1>to1:
        return 0
    elif lastUsedCmd=='B':
        return f(from1+2, to1, 'A')+ f(from1**2,to1,'C')
    else:
        return f(from1+2, to1, 'A')+f(from1+5,to1,'B')+ f(from1**2,to1,'C')
print(f(4,36,'0'))