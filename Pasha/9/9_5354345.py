f = open('ItEge/Pasha/9/9_6.txt')

def triangle(a, b, c):
    if 0 < (a ** 2 + b ** 2 - c ** 2) / (2 * a * b) < 1:
        return True
    return False
cnt = 0
for i in f.readlines():
    s = sorted([x for x in map(int, i.split('\t'))])
    for j in range(len(s) - 2):
        if triangle(s[j], s[j + 1], s[j + 2]):
            cnt += 1
print(cnt)