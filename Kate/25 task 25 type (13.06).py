import re
for i in range(5*(10**5),(10**6)+1):
    cnt=0
    a=[]
    for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                if re.fullmatch(r'\d{3}0',str(j)):
                     cnt+=1
                if j==i**(1/2):
                     continue
                if re.fullmatch(r'\d{3}0',str(i//j)):
                     cnt+=1
    if cnt>45:
         print(i,cnt)
 