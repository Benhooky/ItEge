max5=0
lastn=0 
for n in range(51, 1000):
    s='5' * n
    while '55555' in s:  
        s=s.replace('55555', '88', 1)
        s=s.replace('888', '55', 1)
    if s.count('5')>max5:
        max5=s.count('5')
        lastn = n
print(lastn)