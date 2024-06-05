from string import *
alphabet = digits+ascii_uppercase[:10]
res=[]
for x in alphabet:
    for y in alphabet:
        value=int(f'5{y}4{x}{y}4HJ4',20)+int(f'4{y}6B{y}{x}1',20)
        if value%15==0:
            res.append(x)
x=max(res)
print(int(f'584{x}84HJ4',20)+int(f'486B8{x}1',20))