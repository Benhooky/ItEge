#Создай функцию, которая получает на вход 2 числа
#и находит минимальную степень второго числа, такую
#чтобы первое число было меньше

def f(arg1,arg2):
    step=0
    while arg1>=arg2**step:
        step+=1
    return step


print(f(16,2)) # 5
print(f(10,2)) # 4
print(f(31,5)) # 3
print(f(4,5)) # 1

def f2(arg1):
    if arg1>=100:
        return arg1**(1/2)
    return f2(arg1**2)

print(f2(2))
print(f2(10))