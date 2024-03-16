A = 1
for i in range(10000):
    P = i in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24}
    Q = i in {3, 6, 9, 12, 15, 20, 24, 27, 30}
    f = ((A) <= (P)) and ((not Q) <= (not A))
    if f == 1:
        print(i)