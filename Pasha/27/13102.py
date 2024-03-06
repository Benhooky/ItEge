f = open('ItEge/Pasha/27/27-A_13102.txt')
k = int(f.readline())
n = int(f.readline())
mx = 0
s = [int(x) for x in f.readlines()]
for i in range(len(s) - 2):
    for j in range(i+1,len(s) - 1):
        for l in range(j+1,len(s)):
            if (j - i  == 2 * k) or (l - i == 2 * k) or (l - j == 2 * k):
                mx = max(mx, s[i] + s[j] + s[l])
print(mx)