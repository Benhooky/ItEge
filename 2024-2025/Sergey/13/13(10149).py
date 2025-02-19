from ipaddress import ip_network, ip_address
for mask in range(1,33):
    net = ip_network(f"220.128.112.142/{mask}",strict=False)
    if net.network_address==ip_address("220.128.96.0"):
        print(mask)
        print(net.netmask)