P = list(range(56, 79))
Q = list(range(63, 85))
A = []

for x in range(100):
    if not(((not(x in P)) <= (x in Q)) <= ((x not in Q) <= (x in A))):
        A.append(x)

print(A)
#7