def f(x, y, h):
    if (h == 5  or h==3)and x + y >= 61:
        return 1
    elif h == 5 and x + y < 61:
        return 0
    elif x + y >= 61 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y , h + 1) or f(x, y + 1, h + 1) or f(x * 4, y, h + 1) or f(x, y * 4, h + 1)   
        else:
            return f(x + 1, y , h + 1) and f(x, y + 1, h + 1) and f(x * 4, y, h + 1) and f(x, y * 4, h + 1)   
for x in range(1, 57):
    if f(3, x, 1) == 1:
        print("Задача 19:", x)

