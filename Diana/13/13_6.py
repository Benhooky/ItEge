from ipaddress import *
ipNet= ip_network('171.128.0.0/255.128.0.0')
cnt=0
for ip in ipNet:
    binIp=f'{ip:b}'
    if binIp[:16].count('1')<binIp[16:].count('1'):
        cnt+=1
print(cnt)