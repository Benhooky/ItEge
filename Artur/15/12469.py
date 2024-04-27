answerLst = []
for Aleft in range(1, 105):
    for Aright in range(Aleft + 1, 105):
        flag = True
        for x in range(1, 300):
            x/=2
            if not((7 <=x <= 68) <= (((not(29 <=x <= 100)) and (not(Aleft <= x <= Aright))) <= (not(7 <= x <= 68)))):
                flag = False
                break
        if flag:
            answerLst.append(Aright - Aleft)
print(min(answerLst))