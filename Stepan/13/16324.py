from ipaddress import *
cnt = 0
net = ip_network('122.159.136.144/255.255.255.248', strict = False)
for ip in net:
    bin_ip = f'{ip:b}'
    if bin_ip.count('1')%4!=0:
        cnt += 1
print(cnt)
