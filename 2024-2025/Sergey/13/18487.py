from ipaddress import ip_network
for A in range(0,256):
    net=ip_network(f'192.214.{A}.184/255.255.255.224',strict=False)
    cntGood = 0
    cntIp = 0
    for ip in net:
        cntIp += 1
        binIp=f"{ip:b}"
        if binIp.count("1")>15:
            cntGood += 1
    if cntGood == cntIp:
        print(A)
    
    flag = True
    for ip in net:
        cntIp += 1
        binIp=f"{ip:b}"
        if binIp.count("1")<=15:
            flag = False
            break
    if flag:
        print(A)

    
for A in range(0,256):
    net=ip_network(f'192.214.{A}.184/255.255.255.224',strict=False)
    if all(f'{ip:b}'.count('1')>15 for ip in net):
        print(A)