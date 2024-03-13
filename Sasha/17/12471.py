f = open('ItEge/Sasha/17/17_12471 (3).txt')
lis = [int(x) for x in f]
max13 = -10000000000
cnt = 0
avgSum = 0
for i in lis:
    #1
    '''
    if str(i)[-2:]=='13':
        max13 = max(max13,i)
    '''
    #2
    if i%100==13:
        max13 = max(max13,i)
for i in range(len(lis)-2):
    helper = [lis[i],lis[i+1],lis[i+2]]
    #1
    '''
    if all(x%2==0 for x in helper) or any(len(str(abs(x)))==2 for x in helper):
        if sum(helper)<=max13:
            cnt+=1
            avgSum+=sum(helper)
    '''
    #2
    if (helper[0]%2==0 and helper[1]%2==0 and helper[2]%2==0) or len(str(abs(helper[0])))==2 or len(str(abs(helper[1])))==2 or len(str(abs(helper[2])))==2:
        if sum(helper)<=max13:
            cnt+=1
            avgSum+=sum(helper)
print(cnt,avgSum//cnt)