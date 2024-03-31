from ipaddress import *
net = ip_network('203.111.195.0/255.255.240.0',strict=False)
cnt = 0
for ip in net:
    binIp = f'{ip:b}'
    if binIp.count('0')%3==0:
        if '000' in binIp and '111' in binIp:
            cnt+=1
print(cnt)