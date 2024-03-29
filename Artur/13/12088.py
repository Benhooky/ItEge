from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0')
count = 0
for ip in net:
    binIp = f'{ip:b}'
    count1 = binIp[:16].count('1')
    count0 = binIp[16:].count('0')
    if count0 % 2 == 1:
        if count1 <= count0:
            count += 1 
print(count)