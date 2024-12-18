from ipaddress import ip_address, ip_network
for mask in range(1,32):
    net1 = ip_network(f"216.54.187.235/{mask}",strict=False)
    net2 = ip_network(f"216.54.174.128/{mask}",strict=False)
    if net1.network_address != net2.network_address:
        if net1.broadcast_address != net1.network_address:
            if net2.broadcast_address != net2.network_address:
                print(mask)