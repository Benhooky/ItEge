from ipaddress import *
net = ip_network("255.255.252.0/156.132.15.138",strict=False)
cnt=0
for ip in net:
    binIp=f"{ip:b}"
print(net)