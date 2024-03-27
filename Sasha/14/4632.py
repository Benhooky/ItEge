f = 8**1006+5**1947+505
s = ''
d = 7
sum6 = 0
sum2 = 0
while f>0:
    s = str(f%d) + s
    f//=d
#1
for i in s:
    if i=='6':
        sum6+=6
    elif i=='2':
        sum2+=2
#2
print(s.count('6')*6 - s.count('2')*2)
#3
sum6 = sum(int(x) for x in s if x=='6')
sum2 = sum(int(x) for x in s if x=='2')
print(sum6-sum2)