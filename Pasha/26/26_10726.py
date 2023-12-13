f = open('ItEge/Pasha/26/26_10726.txt')
n = int(f.readline())
s = sorted([[int(x) for x in d.split()] for d in f.readlines()])
slov = {s[0][0]:s[0][1]}
for i in s[1:]:
    for j in slov.items():
        if i[0] <= j[1] and i[1]>j[1]:
            slov[j[0]] = i[1]

