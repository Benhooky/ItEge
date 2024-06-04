s=11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
lst=[]
while s>0:
    lst=[s%15]+lst
    s=s//15
print(len(set(lst)))
