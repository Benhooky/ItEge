for x in "0123456789ABCDEFGHI"[::-1]:
    a1 = int("98897"+x+"21",19)
    a2 = int("2"+x+"923",19)
    if (a1+a2)%18==0:
        print((a1+a2)//18)
        break