s = []
def f(from1,to1,AlreadyUsed):
    AlreadyUsed = AlreadyUsed[::]
    if from1==to1:
        return 1
    if from1>to1 or from1 in AlreadyUsed:
        return 0
    if from1<to1:
        AlreadyUsed.append(from1-3)
        AlreadyUsed.append(from1*3)
        return f(from1-3,to1,AlreadyUsed) + f(from1*3,to1,AlreadyUsed)
print(f(3,30,s))