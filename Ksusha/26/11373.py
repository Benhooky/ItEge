f = open('ItEge/Ksusha/26/26_11373.txt')
N = int(f.readline())
K = int(f.readline())
people=[]
tables = K*[0]
times = sorted([[int(x) for x in line.split()] for line in f],key = lambda x:x[2])
for person in times:
    if person[0]<=1320:
        if tables[person[1]-1]<person[0]:
            tables[person[1]-1] = person[0] + 120
            people.append(person[1])
        else:
            for i in range(K):
                if tables[i]<person[0]:
                    tables[i] = person[0] + 120
                    people.append(i+1)
                    break
print(len(people),people[-2])