class1 = ['Егор', 'Миша', 'Лёша', 'Саша', 'Максим',423234,345645]
print('class1',class1, id(class1))
class1.pop() # удаление элемента по индексу
print('class1',class1, id(class1))
print(class1[0],class1[1])
class1.append('Игорь') # добавление элемента в конец
print(class1[3],class1[-1])
class1.sort() # сортирует по возрастанию
print('class1',class1, id(class1))
class1.sort(reverse=True) # сортирует по убыванию
print('class1',class1, id(class1))
class1.insert(2,'Андрей') # вставка элемента по индексу
print('class1',class1, id(class1))
class1.remove('Андрей') # удаление элемента по значению
print('class1',class1, id(class1))
newClass = class1[0:3]
print('newClass',newClass, id(newClass))
secondClass = class1
print('secondClass',secondClass, id(secondClass))
secondClass.pop()
print('secondClass',secondClass, id(secondClass))
print('class1',class1, id(class1))
secondClass = class1.copy()
print('secondClass',secondClass, id(secondClass))