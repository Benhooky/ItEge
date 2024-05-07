f = [int(x) for x in open("ItEge/Igor/var4/17var04.txt")]
mni1=200000
cnt=0
min700 = min(x for x in f if str(x).endswith('700')) 
for e in range(len(f)-2):
    troika = [f[e],f[e+1],f[e+2]]
    if len([x for x in troika if 10000<=abs(x)<=99999]) <= 2 :
        if sum(troika) >= min700:
            cnt+=1
            mni1=min(mni1,sum(troika))
print(cnt,mni1)