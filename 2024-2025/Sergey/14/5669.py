from string import ascii_uppercase,digits
alph=(digits + ascii_uppercase)[:16]
for x in alph:
    sum1=int(f"8569{x}",16)+int(f"12{x}48",16)
    sum1=oct(sum1)[2:]
    chet=0
    for elem in sum1:
        if elem in "0246":
            chet+=1
    if chet<=2:
        print(sum1)