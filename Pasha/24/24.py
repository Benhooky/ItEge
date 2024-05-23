file = open('ItEge/Pasha/24/24_4643.txt').readline()
file = file.replace('1', '*')
file = file.replace('2', '*')
file = file.replace('A', '@')
file = file.replace('B', '@')
s = file[0]
mx = 0
for i in range(1, len(file)):
    s += file[i]
    if len(s)%3 == 0:
        if s[-3:] != '**@':
            mx = max(mx, len(s)-3)
            s = ""
    elif len(s)%3 == 1:
        if s[-4:] != '**@*':
            mx = max(mx, len(s)-1)
            s = s[-1]
    elif len(s)%3 == 2:
        if s[-5:] != '**@**':
            mx = max(mx, len(s)-2)
            s = s[-2:]
print(mx//3)