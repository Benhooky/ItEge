from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240')
k = 0
for x in net:
    two = bin(int(x))[2:].zfill(32)
    if two.count('1') % 2 == 0:
        k += 1
print(k)