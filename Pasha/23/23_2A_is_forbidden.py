#Нельзя использовать команду A два раза подряд
def F(from1,to1,lastUsedCommand):
    if from1 > to1:
        return 0
    elif from1 == to1 :
        return 1
    else:
        if lastUsedCommand == 'А':
            return F(from1+3,to1, 'B') + F(from1*2,to1, 'C')
        else:
            return F(from1 + 2, to1, 'A') + F(from1+3,to1, 'B') + F(from1*2,to1, 'C')
print(F(3,20,'X'))