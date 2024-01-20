f = open("ItEge/Danila/17/17_12249 (1).txt")
array = [int(x) for x in f]
max3 = 0
cnt = 0
sumA = 0
for i in array:
    if abs(i) % 10 == 3 and 9999 < abs(i) < 100000:  
        max3 = max(max3, i) 
for i in range(len(array) - 2):
    myTriple = [array[i], array[i + 1], array[i + 2]]
    if any(abs(x) % 10 == 3 for x in myTriple):
        if (sum(myTriple)) <= max3: 
            sumA = max(sum(myTriple), sumA) 
            cnt += 1
print(cnt, sumA)
