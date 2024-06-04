import itertools
s = itertools.permutations("АССЕМБЛЕР", 9)
cnt = 0
arl = []
for e in s:
    arl.append("".join(e))
arl = set(arl)
glas = "АЕ"
for e in arl:
    sumWord = 0
    for letter in range(len(e)):
        if e[letter] in glas:
            sumWord += letter + 1
    if sumWord == 9:
        cnt+=1
print(cnt)