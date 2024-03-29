f = [int(x) for x in open('ItEge/Danila/17/17_12926 (5).txt')]
A = -1000000000
max2 = -1000000000
cnt = 0
minSum = 10000000000000
for i in range(len(f)-3):
    quatro = [f[i],f[i+1],f[i+2],f[i+3]]
    #1
    if abs(quatro[0])%10==abs(quatro[1])%10==abs(quatro[2])%10==(quatro[3])%10:
        A = max(A,sum(quatro))
    #2
    # if all(abs(x)%10==abs(quatro[0])%10 for x in quatro):
    #     A = max(A,sum(quatro))
#1
for x in f:
    #1
    # if len(str(abs(x))) == 2:
    #2
    if 9<abs(x)<100:
        max2 = max(max2,x)
#2
#max2 = max(x for x in f if 9<abs(x)<100)
for i in range(len(f)-4):
    five = [f[i],f[i+1],f[i+2],f[i+3],f[i+4]]
    #1
    cntLower = 0
    for element in five:
        if element<A:
            cntLower+=1
    #2
    #cntLwr = sum(1 for x in five if x<A)
    if cntLower == 1:
        if abs(sum(five))%max2==0:
            cnt+=1
            minSum = min(minSum,sum(five))
print(cnt,minSum)