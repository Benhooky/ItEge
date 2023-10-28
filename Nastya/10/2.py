

"""
print(int('1110110', 2))
print(bin(4234))#2
print(oct(3123))#8
print(hex(231))#16

print(oct(55)[2:])
print(oct(83)[2:])
print(oct(91)[2:])

print(int('81', 16))
print(int('203', 8))
print(int('1111111', 2))

print(bin(100)[2:])
print(bin(90)[2:])
print(bin(80)[2:])
"""

#Надо вывести на экран все чётные числа [2,30]

for x in range(2, 31):
    if x%2==0:
        print(x)
        
for x in range(2, 31,2):
    print(x)
    

