from ipaddress import ip_network
net = ip_network('192.168.32.64/255.255.255.192',strict = False)
cnt=0
for ip in net:
    binIp = f'{ip:b}'
    if binIp[-3:]=='101':
        cnt+=1
print(cnt)