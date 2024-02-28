number= 18*7**108-5*49**76+343**35-50
s = []
while number>0:
    s.append(number%49)
    number//=49
print(s)