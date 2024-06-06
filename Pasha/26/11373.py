file = open('ItEge/Pasha/26/26_11373 (2).txt')
n = int(file.readline())
k = int(file.readline())
sl = {x:0 for x in range(1, k + 1)}
spis = sorted([[x for x in map(int, i.split())] for i in file], key=lambda x:x[2])
leastAnswers = []
for person in spis:
    if person[0] <= 1320:
        if person[0] > sl[person[1]]:
            sl[person[1]] = person[0] + 120
            leastAnswers.append(person[1])
        else:
            for j in range(1, k + 1):
                if sl[j] < person[0]:
                    sl[j] = person[0] + 120
                    leastAnswers.append(j)
                    break
print(len(leastAnswers), leastAnswers[-2])