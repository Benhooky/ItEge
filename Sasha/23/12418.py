
def f(from1, to1, cntA):
    if from1>to1+4 or cntA > 2:
        return 0
    if from1==to1:
        return 1
    return f(from1 - 2,to1, cntA+1) + f(from1 * 2, to1, cntA) + f(from1 * 3, to1, cntA)
print(f(6,48,0))

