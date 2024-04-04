from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.192', strict=False)
cnt = 0
for ip in net:
    binIp = f'{ip:b}'
    if f'{ip:b}'.count('1')% 5 !=0:
        cnt+=1
print(cnt)
