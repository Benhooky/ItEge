def F(from1,to1):
    if from1>to1 or from1==8:
        return 0
    elif from1==to1:
        return 1
    else:
        return F(from1+1,to1)+F(from1+3,to1)+F(from1*2,to1)
print(F(1,10)*F(10,20)*F(20,35))