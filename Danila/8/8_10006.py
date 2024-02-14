from itertools import product
cnt = 0
for i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
    print(cnt,i)
    cnt+=1
arl = ["".join(x) for x in product("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", repeat=8)]
print(arl.index("РЕКУРСИЯ")+1)

