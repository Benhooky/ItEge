from ipaddress import *
net = ip_network('185.8.0.0/255.255.128.0')
maxCnt1 = 0
for ip in net:
    binIp = f'{ip:b}'
    maxCnt1 = max(maxCnt1,binIp.count('1'))
print(maxCnt1)