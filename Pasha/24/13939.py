f = open('ItEge/Pasha/24/24_13939.txt').readline()
f = f.replace('A','*')
f = f.replace('B','*')
f = f.replace('C','*')
f = f.replace('D','*')
f = f.replace('E','*')
f = f.replace('3','*')
f = f.replace('4','*')
keeperS = ''
cnt = 0
for element in f:
    keeperS+=element
    while keeperS[0]=='0' or keeperS[0]=='*':
        keeperS=keeperS[1:]
        if len(keeperS)==0:
            break
    if keeperS[-1]=='*':
        cnt+=1
        keeperS=''
print(cnt)