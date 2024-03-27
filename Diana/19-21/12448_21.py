def f(first, second, turn):
    if first * second >= 777:
        if turn == 2 or turn==4:
            return True
        else:
            return False
    elif turn > 4:
        return False
    else:
        if turn % 2 == 0:
            return (f(first + 3, second, turn + 1)
                    and f(first * 2, second, turn + 1)
                    and f(first, second + 3, turn + 1)
                    and f(first, second * 2, turn + 1))
        else:
            return (f(first + 3, second, turn + 1)
                    or f(first * 2, second, turn + 1)
                    or f(first, second + 3, turn + 1)
                    or f(first, second * 2, turn + 1))
for s in range(1, 110):
    if f(7, s, 0):
        print(s)
print("---")
def F(first, second, turn):
    if first * second >= 777:
        if turn == 2 :
            return True
        else:
            return False
    elif turn > 2:
        return False
    else:
        if turn % 2 == 0:
            return (F(first + 3, second, turn + 1)
                    and F(first * 2, second, turn + 1)
                    and F(first, second + 3, turn + 1)
                    and F(first, second * 2, turn + 1))
        else:
            return (F(first + 3, second, turn + 1)
                    or F(first * 2, second, turn + 1)
                    or F(first, second + 3, turn + 1)
                    or F(first, second * 2, turn + 1))
for s in range(1, 110):
    if F(7, s, 0):
        print(s)
print("Answer=33")