from ipaddress import *
listansw=[]
net = ip_network(f"129.128.0.0/255.128.0.0",strict=True)
for ip in net.hosts():
    binIp=f"{ip:b}"
    cnt=binIp.count("0")
    listansw.append(cnt)
print(min(listansw))