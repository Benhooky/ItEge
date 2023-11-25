from math import sqrt


def g(x, y, turn):
    if sqrt(x**2 + y**2) >= 13 and turn == 2:
        return 1

    elif sqrt(x**2 + y**2) < 13 and turn == 2:
        return 0

    elif sqrt(x**2 + y**2) >= 13:
        return 0
    if turn % 2 == 0:
        return g(x + 3, y, turn + 1) or g(x, y + 3, turn + 1) or g(x, y + 4, turn + 1)

    else:
        return g(x + 3, y, turn + 1) or g(x, y + 3, turn + 1) or g(x, y + 4, turn + 1)


for S in range(1, 13):
    if g(S, 2, 0):
        print(S)
