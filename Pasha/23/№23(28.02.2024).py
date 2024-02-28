a = set()
for i in range (0,16):#вперёд 10
    j = 15-i#назад 5
    a.add(i*10-5*j)
print(len(a))