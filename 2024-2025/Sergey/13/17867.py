from ipaddress import ip_network
net = ip_network('172.16.168.0/255.255.248.0',strict = False)
cnt=0
for ip in net:
    binIp = f'{ip:b}'
    if binIp.count('1')%5!=0:
        cnt+=1
print(cnt)