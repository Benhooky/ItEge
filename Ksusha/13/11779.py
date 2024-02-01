from ipaddress import *
net=ip_network("151.192.0.0/255.224.0.0",1)
cnt=0
for ip in net:
    if f'{ip:b}'.count('1')==f'{ip:b}'.count('0'):
        cnt+=1
print(cnt)