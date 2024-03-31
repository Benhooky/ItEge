f=open('ItEge/Ksusha/27/27A_11604.txt')
K=int(f.readline())
n=int(f.readline())
lst=[int(x) for x in f]
cnt = 0
for i1 in range(n-4*K):
    for i2 in range(i1+K,n-3*K):
        for i3 in range(i2+K,n-2*K):
            for i4 in range(i3+K,n-K):
                for i5 in range(i4+K,n):
                    if f'{lst[i1]:b}'.count('1')==f'{lst[i2]:b}'.count('1')==f'{lst[i3]:b}'.count('1')==f'{lst[i4]:b}'.count('1')==f'{lst[i5]:b}'.count('1'):
                        cnt+=1
print(cnt)