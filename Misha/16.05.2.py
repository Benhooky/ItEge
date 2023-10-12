f = open('Misha/inf_22_10_20_27b.txt')
n = int(f.readline())
summ = 0
raznica3 = [1000000,1000000]
for i in range(n):
    a, b = f.readline().split()
    a = int(a)
    b = int(b)
    summ += min(a, b)
    r1 = abs(a-b)
    if r1 % 3 != 0:
        if r1%3==1:
            raznica3[0]=min(raznica3[0],r1)
        elif r1%3==2:
            raznica3[1]=min(raznica3[1],r1)
if summ%3==1:
    summ+=raznica3[1]
elif summ%3==2:
    summ+=raznica3[0]
print(summ)