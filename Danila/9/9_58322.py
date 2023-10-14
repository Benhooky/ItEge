my_values = [sorted([int(x) for x in line.split()])
             for line in open("ItEge/Danila/9/9_58322.txt")]
cnt = 0
for line in my_values:
    a = [line[x] - line[x-1] for x in range(1, len(line))]
    if (line[-1]**2 > line[0] * line[1] * line[2]) or (all(x == a[0] for x in a)):
        cnt += 1
print(cnt)
