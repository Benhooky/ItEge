from string import ascii_uppercase,digits
alph =  (digits + ascii_uppercase)[:27]
for x in alph:
    f = int('8'+x+'38'+x+"68",27) +  int('37'+x+'3163',27)
    if f%26==0:
        print(f//26)