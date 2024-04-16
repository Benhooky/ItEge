from ipaddress import *
net =ip_network('192.168.76.160/255.255.255.240')
cnt=0
for ip in net:
    binIp=f'{ip:b}'
    #print(binIp)
    if binIp[-1]=='0':
        if binIp[-8:].count('1')%2==0:
            cnt+=1
            print(binIp)
print(cnt)