def f(from1,to1, allUsed):
    if from1 == to1:
        return 1
    elif from1 < to1:
        return 0
    else:
        if allUsed[-2:] == 'AA':
            return f(from1/2 if from1%2 == 0 else from1 - 7, to1, allUsed + 'B')
        elif allUsed[-2:] == 'BB':
            return f(from1 - 2, to1, allUsed + 'A')
        else:
            return f(from1 - 2, to1,  allUsed + 'A') + f(from1/2 if from1%2 == 0 else from1 - 7, to1, allUsed + 'B')

print(f(40,1,''))