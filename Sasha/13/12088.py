from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0')
cnt = 0 
for ip in net:
    binIp = f'{ip:b}'
    if binIp[16:32].count('0')% 2 == 1:
        if binIp[0:16].count('1')<=binIp[16:32].count('0'):
            cnt+=1
print(cnt)