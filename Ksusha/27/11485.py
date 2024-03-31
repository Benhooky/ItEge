f = open("ItEge/Ksusha/27/27-A_11485 (1).txt")
N = int(f.readline())
lst = [int(x) for x in f]
A = lst[:N]
B = lst[N:]
minDiff = 100000000000000000
for i in range(N):
    for j in range(N):
        minDiff = min(minDiff,abs(A[i]-B[j]))
print(minDiff)