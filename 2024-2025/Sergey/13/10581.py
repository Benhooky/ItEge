from ipaddress import ip_address, ip_network 
cntMask = 0
for mask in range(1,33):
    net = ip_network(f'175.122.80.13/{mask}',strict=False)
    cntIpS = 0
    if net.network_address == ip_address('175.122.80.0'):
        for ip in net:
            cntIpS += 1
        if cntIpS >= 28:
            cntMask += 1
print(cntMask)