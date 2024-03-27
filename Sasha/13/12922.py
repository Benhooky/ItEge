from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248')
cnt = 0
for ip in net:
    binIp = f'{ip:b}'
    if '101' not in binIp:
        cnt+=1
print(cnt)