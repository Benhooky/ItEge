from string import ascii_uppercase,digits
answers = []
alph =  (digits + ascii_uppercase)[:16]
for x in alph:
    for y in alph:
        f = int('27'+"A"+x+'23',16) +  int('8'+y+"E"+"5"+"D"+"2",16)
        if f%5==0:
            s=(int(x,16)+int(y,16))
            answers.append(s)
print(max(answers))