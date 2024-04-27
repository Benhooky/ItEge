from ipaddress import *
lstAnswer = []
for A in range(0,256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', strict=False)
    flag = True
    for ip in net:
        binIp = f"{ip:b}"
        if binIp[:16].count('1')<binIp[16:].count('1'):
            flag = False
            break
    if flag:
        lstAnswer.append(A)
print(max(lstAnswer))