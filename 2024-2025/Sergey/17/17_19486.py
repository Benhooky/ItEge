mas=[int(x) for x in open("ItEge/2024-2025/Sergey/17/17_19486.txt")]
cnt=0 
maxSum=-100000000
chet7=0
for x in mas:
    if abs(x)%10==7:
        chet7+=1
for i in range(len(mas)-1):
    if mas[i]<0 and mas[i+1]>0 or mas[i]>0 and mas[i+1]<0:
        if mas[i]+mas[i+1]<chet7:
            cnt+=1
            maxSum=max(maxSum,mas[i]+mas[i+1])
print(cnt,maxSum)