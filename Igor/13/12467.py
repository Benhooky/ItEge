from ipaddress import *
cnt = 0
for A in range(0,256):
    net = ip_network(f"246.81.65.{A}/255.255.255.224",strict=False)
    flag=True
    for ip in net:
        binip=f"{ip:b}"
        if not(binip[16:24].count('0')>binip[24:].count('0')):
            flag=False
            break
    if flag:
        cnt+=1
print(cnt)