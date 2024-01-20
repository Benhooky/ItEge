f = open("ItEge/Danila/17/17_12471.txt")
array = [int(x) for x in f]
max13 = 0
cnt = 0
sumA = 0
for i in array:
    if abs(i) % 100 == 13:  
        max13 = max(max13, i)
for i in range(len(array) - 2):
    myTriple = [array[i], array[i + 1], array[i + 2]]
    if all(x%2==0 for x in myTriple) or any(len(str(abs(x)))==2 for x in myTriple):
        if (sum(myTriple)) <= max13:
            sumA += sum(myTriple)
            cnt += 1
print(cnt, sumA // cnt)
