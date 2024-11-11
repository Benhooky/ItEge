from string import ascii_uppercase,digits
alph =  (digits + ascii_uppercase)[:8]
for x in alph:
    f = int(f'{x}1{x}',16) +  int(f'{x}3{x}3',8)
    while f%2==0:
        f//=2
    if f==1:
        print(x)