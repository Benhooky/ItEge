f = [str(x) for x in open("dz/17_2008.txt")]
cnt=0
listansw=[]
for i in range(len(f)-1):
    if (((f[i][-2]) == "4" or (f[i][-2]) == "3" or (f[i][-2]) == "2" or (f[i][-2]) == "1" or (f[i][-2]) == "0")
        and ( ((f[i][-3]) == "3") or (f[i][-3]) == "4" or (f[i][-3]) == "5" or (f[i][-3]) == "6" or (f[i][-3] )== "7"  )):
            cnt+=1
            Fint=int(f[i])
            listansw.append(Fint)
print(cnt,min(listansw))