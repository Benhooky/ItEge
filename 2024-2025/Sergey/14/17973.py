from string import ascii_uppercase,digits
alph =  (digits + ascii_uppercase)[:24]
for x in alph:
    f = int('12'+x+'734',24) +  int('8'+x+'95'+x+'3',24) +  int('24'+x+'796',24)
    if f%23==0:
        print(f//23)