def F(n, m , k):
    if n + m > k and m + k > n and n + k > m:
        return True
    return False
for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if not((F(x, 10, 20) <= (not(max(x, 8) > 24))) == (not(F(3, A, x)))):
            flag = False 
            break 
    if flag:
        print(A)
