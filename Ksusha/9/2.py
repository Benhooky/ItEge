a = open("ItEge/Ksusha/9/0000.txt")
cnt = 0
for myStr in a:
    myStr = sorted([int(i) for i in myStr.split()])
    if ((myStr[3]) ** 2) > (myStr[2] * myStr[1] * myStr[0]) or (
        myStr[3] - myStr[2]
    ) == (myStr[2] - myStr[1]) == (myStr[1] - myStr[0]):
        cnt += 1
print(cnt)
