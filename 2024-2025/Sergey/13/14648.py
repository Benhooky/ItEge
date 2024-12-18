from ipaddress import ip_address, ip_network
for mask in range(1,32):
    net = ip_network(f"218.48.192.56/{mask}",strict=False)
    cnt = 0
    if net.network_address == ip_address('218.48.192.0'):
        for ip in net:
            cnt+=1
        if cnt >= 500:
            print(net.netmask)