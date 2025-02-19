from sys import getsizeof as size
a = 'Артём' #str
print(a,id(a))
b = ["Артём"] #list
print(f'b = {id(b)}')
print(id(b[0]))
c = ["Артём"] #list
print(id(c))
print(id(c[0]))

d = 5 #int
g = 5 #int
print(id(d), id(g))

d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
d+=1
print(id(d), id(g))
b.append("Егор")
print(f'b = {id(b)}')
a = a[:3]
print(a,id(a))
a = 5
print(a,id(a))
a += 3
print(a,id(a))
print('size',size(a))
ad = True
print(ad,id(ad))
ad = False
print(ad,id(ad))
print(size(ad))
mas = [345345, 543534, True]
print(mas,id(mas), size(mas))
print(size(mas[0]), size(mas[1]), size(mas[2]) )
print(size('zaawdwadwaddwa'))
mas[0] = 1111

tup = (1,-4,5)
print(tup,id(tup), size(tup))
tup = (1,-4,9)
print(tup,id(tup), size(tup))

A = {1,2,4}
B = {4,8,9}
C = A.intersection(B)
print(C)