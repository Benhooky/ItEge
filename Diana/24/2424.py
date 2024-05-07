
f=open('ItEge/Diana/24/24_2 .txt').readlines()
keeperS=''
maxLen=0
for string in f:
    lst=string.replace('XYZ',' XYZ ').split()
    cnt=0
    for x in lst:
        if x=='XYZ':
            cnt+=3
        else:
            maxLen=max(maxLen,cnt)
            cnt=0
print(maxLen)
