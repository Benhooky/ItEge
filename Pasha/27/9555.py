f = open('ItEge/Pasha/27/27_A_9555.txt')
n, k = map(int, f.readline().split())
s = [int(x) for x in f]
x = 0
for i in range(len(s) - k + 1):
    for j in range(i + k, len(s)+1):
        if sum(s[i:j]) % 111 == 0:
            x += 1
print(x)