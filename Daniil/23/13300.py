def f(from1,to1):
    if from1 < to1:#мы уже не дойдем до пункта назначения
        return 0
    if from1 == to1:#мы дошли до пункта назначения
        return 1
    if from1>to1:#мы еще не дошли до пункта назначения, продолжаем идти
        return f(from1-1,to1)+f(from1-2,to1)+f(from1//4,to1)
print(f(26,20)*f(20,3))