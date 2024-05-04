f = [int(x) for x in open("probnik/17var04.txt")]
mni1=200000
cnt=0
max700 = min(x for x in f if str(x).endswith('700')) 
for e in range(len(f)-2):
    if ( (len(str(f[e]))==5 and len(str(f[e+1]))==5) or (len(str(f[e]))==5 and len(str(f[e+2]))==5) or (len(str(f[e+1]))==5 and len(str(f[e+2]))==5) or (len(str(f[e]))==5) or (len(str(f[e+1]))==5) or (len(str(f[e+2]))==5)):
        if f[e] + f[e+1] + f[e+2] >= max700:
            cnt+=1
            mni1=min(mni1,f[e] + f[e+1] + f[e+2])
print(cnt,mni1)