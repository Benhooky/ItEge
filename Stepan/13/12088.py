from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0', strict = False)
cnt = 0
for ip in net:
    binip = f'{ip:b}'
    if binip[:16].count('1') <= binip[16:].count('0') and binip[16:].count('0') %2 != 0:
        cnt +=1
print(cnt)