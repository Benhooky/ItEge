from math import log10
for n in range (2000,1,-1):
    k=0
    s='1'+'5'*n+'2'+'5'*n
    while ('15' in s) or ('255' in s)or ('555' in s):
        if '15' in s:s= s.replace('15','2',1)
        if '255' in s:s=s.replace('255','1',1)
        if '555' in s: s=s.replace('555','12',1)
    for i in s:
        k+=int(i)
    if int(log10(k))==2:
        print(n) 
        break
    
        
