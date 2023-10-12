f = [int(x)
     for x in open('D:/Progs/Python/EgeInf/Pasha/17_2024.txt').readlines()]
max13 = 0
maxsum = 0
count = 0
cnt3 = 0
triple = [0, 0, 0]
for i in f:
    if str(i)[-2:] == '13':
        max13 = max(max13, i)
for j in range(len(f)):
    if 99 < triple[0] < 1000:
        cnt3 -= 1
    triple[0] = triple[1]
    triple[1] = triple[2]
    triple[2] = f[j]
    if 99 < triple[2] < 1000:
        cnt3 += 1
    if cnt3 == 2:
        if sum(triple) <= max13:
            count += 1
            maxsum = max(maxsum, sum(triple))
print(count, maxsum)
