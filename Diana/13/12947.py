from ipaddress import *
net = ip_network('203.111.195.0/20',strict=False)
cnt = 0
for ip in net:
    binIp = f'{ip:b}'
    if binIp.count('0')%3==0 and '111' in binIp and '000' in binIp:
        cnt+=1
print(cnt)