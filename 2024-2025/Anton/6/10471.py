arr = [
    (1, 2),
    (11, 2),
    (1, 12),
    (11, 12),
    (-11, -12),
    (-11, 12),
    (-12, 11),
    (10, 10),
    (10, 5),
]
for A in range(-1000, 1000):
    yesCounter = 0
    for s, t in arr:
        if s > 10 or t > A:
            yesCounter += 1
    if yesCounter == 7:
        print(A)