import csv
f = open("Pasha/9_2024.txt")
count = 0
reader = csv.reader('Pasha/09_10910.csv')
for i in reader:
    j = ([x for x in (map(int, i.split('\t')))])
    cnt = 0
    sr = 0
    for a in set(j):
        if j.count(a) == 2:
            cnt += 1
            sr += a
        if cnt > 2:
            break
    if cnt == 2 and sr / 2 < sum(j) / 7:
        count += 1
print(count)
