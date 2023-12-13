from ipaddress import *
net = ip_network('112.154.133.208/255.255.252.0',0)
cnt=0
for ip in net:
    f = f'{ip:b}'
    if f[:16].count('1')<=f[16:].count('0') and f[16:].count('0')%2!=0:
        cnt+=1
print(cnt)