s = open("ItEge/Igor/17/17_9840.txt").read()
max39 = 0
cnt = 0
maxsum = 0
list1 = [x for x in s.split()]
for i in list1:
    if len(i) == 4 and i[-2:] == "39":
        max39 = max(int(i), max39)
for i in range(len(list1)-1):
    if ((len(list1[i]) == 4) ^ (len(list1[i+1]) == 4)):
        if (int(list1[i])+int(list1[i+1]))**2 <= max39**2:
            cnt += 1
            maxsum = max(int(list1[i])+int(list1[i+1]), maxsum)
print(cnt, maxsum)
