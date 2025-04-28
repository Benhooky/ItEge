from ipaddress import ip_address, ip_network
for mask in range(0,33):
    net = ip_network(f'215.181.192.0/{mask}',strict=False)
    if ip_address('215.181.200.27') in net:
        print(net.netmask)