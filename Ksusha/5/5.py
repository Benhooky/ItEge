r = 0
for N in range(1, 1000):
    s = bin(N)[2:]
    if N % 3 == 0:
        s += s[-3:]
    else:
        s += bin(N % 3*3)[2:]
    R = int(s, 2)
    if R <= 137:
        r = max(R, r)
print(r)
