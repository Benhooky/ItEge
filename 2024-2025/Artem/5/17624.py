minR = 10000000000
for N in range(1,100000):
    R = bin(N)[2:]
    R = R+str(R.count('1')%2)
    R = R+str(R.count('1')%2)
    R = int(R, 2)
    if R > 75:
        minR = min(minR,R)
print(minR)