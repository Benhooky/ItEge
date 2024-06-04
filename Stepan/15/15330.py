answerList = []
for Aleft in range(1,150):
    for Aright in range(Aleft+1,150):
        flag = True
        for x in range(1,300):
            x*=0.5
            if not((47<=x<=115)<=(((not(Aleft<=x<=Aright))and(24<=x<=90))<=(not(47<=x<=115)))):
                flag = False
                break
        if flag:
            answerList.append(Aright - Aleft)
print(min(answerList))