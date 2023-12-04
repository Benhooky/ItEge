from itertools import product

a = product("НИКОЛАЙ", repeat=4)
arl = ["".join(x) for x in a]
glas = "ИОА"
cnt = 0
for word in arl:
    if word[0] != "Й" and any(x in word for x in glas):
        cnt += 1
print(cnt)
