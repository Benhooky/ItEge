f = open("ItEge/Danila/17/17_10100.txt")
array = [int(x) for x in f]
max13 = 0
cnt = 0
sumA = 0
for i in array:
    if abs(i) % 100 == 13:
        max13 = max(max13, i)
for i in range(len(array) - 2):
    myTriple = [array[i], array[i + 1], array[i + 2]]
    if sum(1 if 99<abs(x)<1000 else 0 for x in myTriple) == 2:
        if (sum(myTriple)) <= max13:
            sumA = max(sum(myTriple), sumA)
            cnt += 1
print(cnt, sumA)
