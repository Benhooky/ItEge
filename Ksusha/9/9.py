f=open('ItEge/Ksusha/9/9.txt')
con=0
for my_Str in f:
    lis=sorted(int(i) for i in my_Str.split())
    if (len(set(lis))==7) ^ ((lis[0]+lis[-1])*2<=(sum(lis)-(lis[0]+lis[-1]))*3):
            con+=1
print(con)