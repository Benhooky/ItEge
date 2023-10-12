count = m = 0
f = open('Misha/17.txt')
l = [int(i) for i in f]
min_sp = 0
for i in range(len(l)):
    if abs(l[i]) % 10 == 6:
        min_sp = min(min_sp, l[i])
for i in range(len(l) - 1):
    if ((abs(l[i])%10==6 and (abs(l[i+1]))%10!=6) or ((abs(l[i]))%10!=6 and abs((l[i+1]))%10==6)) and ((l[i]**2+l[i+1]**2) < min_sp**2):
        count += 1
        m = max(m, (l[i]  **2 + l[i+1] **2))
print(count, m)
 