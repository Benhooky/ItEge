f = open("ItEge/Diana/27/27A_15342.txt")
n, k = [int(x) for x in f.readline().split()]
lst = [[int(x) for x in line.split()] for line in f]
res=[]
for i in range(n):
    current = lst[i]
    sumA = sum(
        (
            min(k - abs((current[0] - x[0])), abs(current[0] - x[0])) * (x[1] // 11 + 1)
            if x[1] % 11 != 0
            else min(k - abs(current[0] - x[0]), abs(current[0] - x[0])) * (x[1] // 11)
        )
        for x in lst
        if x != lst[i]
    )
    res.append(sumA)
print(min(res))