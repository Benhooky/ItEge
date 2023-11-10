s = ">"+26*'1'+10*'2'+14*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
sum1 = 0
for i in s[:-1]:
    sum1 += int(i)
print(sum1)
