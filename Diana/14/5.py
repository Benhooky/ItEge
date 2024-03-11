result = 0
for x in range(37):
    for y in range(37):
        sum1 = 0
        f = [2,1,x,4,5,7,y,9][::-1]
        answer = [x,y][::-1]
        xySum = 0
        for i in range(len(f)):
            sum1+=f[i]*37**i
        for i in range(len(answer)):
            xySum+=answer[i]*37**i
        if sum1%36==0:
            result = xySum
print(result)
