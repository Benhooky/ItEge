КоличествоЧисел = 0 
ОбщееКоличество = int(input())
for i in range(ОбщееКоличество):
    НовоеЧисло = int(input())
    if НовоеЧисло % 6 == 0:
        КоличествоЧисел = КоличествоЧисел + 1 
print(КоличествоЧисел)