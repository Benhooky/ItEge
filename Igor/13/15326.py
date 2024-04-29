from ipaddress import *
cnt=0
net = ip_network("105.224.200.224/255.255.255.224",strict=False)
for ip in net:
    binIp = f"{ip:b}"
    if binIp.count("1")%4==0:
        cnt+=1
print(cnt)