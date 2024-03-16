s=open('ItEge/Ksusha/17/17 (6).txt')
lst=[int (x) for x in s]
maxSum=0
SrAr=0
con=0
SrAr=sum(lst)/len(lst)
for i in range(1,len(lst)-2):
    if lst[i]*lst[i+1]>lst[i-1]*lst[i+2]:
        maxSum=max(lst[i]+lst[i+1],maxSum)
        if (lst[i]>SrAr or lst[i+1]>SrAr):
            con+=1
print(maxSum,con)
