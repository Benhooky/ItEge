from ipaddress import *
net = ip_network('192.168.240.0/255.255.255.0')
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if (b.count('1') == b.count('0')):
        cnt += 1
print(cnt)