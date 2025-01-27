#цикл перебирающий числа от 3 до 10
for i in range(3,11):
    print(i)

c = 0
b = 3
if b>4:
    c = 2
print(c)

for i in range(8,1,-3):
    print(i)

mas = [3,5,7,-20,4,12,23,123,234234234,1,231,3,4,546,45,6567,51]
print(mas)
print(mas[1])
print(mas[-1])
mas[2] = 100
print(mas)
mas.append('spichki')
print(mas)
mas.remove('spichki')
print(mas)
mas.pop(3)
print(mas)
mas.remove(3)
print(mas)
mas.insert(3, 334)
print(mas)
mas.sort(reverse=True)
print(mas)
tup = (3,5,7,-20,4,12,23,123,234234234,1,231,3,4,546,45,6567,51)