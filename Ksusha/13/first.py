from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240',strict = False)
cnt = 0
for ip in net:
    bin_ip = f'{ip:b}'
    if bin_ip.count('1')%2==0:
        cnt+=1
print(cnt)

