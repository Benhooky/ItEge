from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240',strict = False)
cnt = 0
for ip in net:
    binIp = f'{ip:b}'
    if binIp.count('1')%2 != 0 :
        cnt+=1
print(cnt)