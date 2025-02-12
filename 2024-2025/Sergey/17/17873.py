f=open("ItEge/2024-2025/Sergey/17/17_17873.txt")
mas=[int(x) for x in f]
minElem=min(mas)
cnt=0
maxSum=-100000000
for i in range(len(mas)-1):
    if mas[i]%16==minElem or mas[i+1]%16==minElem:
        cnt+=1
        maxSum=max(maxSum,mas[i]+mas[i+1])
print(cnt,maxSum)


f=open("ItEge/2024-2025/Sergey/17/17_17873.txt")
mas=[int(x) for x in f]
minElem=min(mas)
cnt=0
maxSum=-100000000
for i in range(len(mas)-2):
    #1
    trig = [mas[i],mas[i+1],mas[i+2]]
    cnt16=sum(1 for x in trig if x%16==minElem)
    #2
    """
    trig = [mas[i],mas[i+1],mas[i+2]]
    for elem in trig:
        if elem%16==minElem:
            cnt16+=1
    """
    #3
    """
    if mas[i]%16==minElem:
        cnt16+=1
    if mas[i+1]%16==minElem:
        cnt16+=1
    if mas[i+2]%16==minElem:
        cnt16+=1
    """
    
    if cnt16==2:
        cnt+=1
        maxSum=max(maxSum,mas[i]+mas[i+1]+mas[i+2])
print(cnt,maxSum)