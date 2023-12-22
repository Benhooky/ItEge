from ipaddress import *
cnt = 0
net = ip_network("192.168.32.48/255.255.255.240",0)
for ip in net:
    f = f'{ip:b}'
    if f.count("1")%2!=0:
        cnt+=1
print(cnt)
