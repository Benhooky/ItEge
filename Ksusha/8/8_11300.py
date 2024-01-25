from itertools import product
d=product('бгдноуш', repeat=6)
cnt=0
answer = 0
d=[''.join(i) for i in d]
for i in d:
    cnt+=1
    if i[0]!='б' and i.count('н')>=2 and 'у' not in i:
        if cnt%2==1 :
            answer = cnt
print(answer)

