from ipaddress import *
listansw=[]
net = ip_network(f"185.8.0.0/255.255.128.0",strict=False)
for ip in net:
    binIp=f"{ip:b}"
    cnt=binIp.count("1")
    listansw.append(cnt)
print(max(listansw))