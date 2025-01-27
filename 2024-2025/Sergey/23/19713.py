def F(from1,to1):
    if from1==to1:
        return 1
    elif from1>to1:
        return 0
    else:
        return F(from1+2,to1) + F(from1*4,to1)
print(F(3,200)*F(200,510))