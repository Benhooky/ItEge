def vir(a, b, c):
    if (a + b == c) or (a + c == b) or (b + c == a):
        return True
    return False
def triangle(a,b,c):
    sides = sorted([a,b,c])
    if sides[-1]<=sides[0]+sides[1]:
        return True
    return False
f = open('ItEge/Pasha/9/913.txt')
cnt = 0
for i in f.readlines():
    s = sorted([x for x in map(int, i.split())], reverse=True)
    flag = True
    flagTriangle = True
    for j in range(len(s) - 2):
        for l in range(j + 1, len(s) - 1):
            for k in range(l + 1, len(s)):
                if vir(s[j], s[l], s[k]):
                    flag = False
                    break
                if not triangle(s[j], s[l], s[k]):
                    flagTriangle = False
                    break
            if not flag:
                break
    if flag and flagTriangle:
        cnt += 1
        print(s)
print(cnt)
