from ipaddress import *
listansw=[]
net = ip_network("10.8.248.131/255.255.224.0",strict=False)
for ip in net:
    binIp=f"{ip:b}"
print(binIp,int(str(binIp),2))
print(net)