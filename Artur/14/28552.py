x = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
set1 = set()
while x>0:
    set1.add(x%6)
    x//=6
print(len(set1))