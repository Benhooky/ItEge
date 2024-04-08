from ipaddress import *
cnt=0
net = ip_network("136.36.240.16/29")
for ip in net:
    binIp = f'{ip:b}'
    if "101" not in binIp:
        cnt += 1
print(cnt)
