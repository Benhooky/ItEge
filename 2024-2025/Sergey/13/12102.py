from ipaddress import ip_network, ip_address
for mask in range(1,33):
    net = ip_network(f"175.184.52.103/{mask}",strict=False)
    if net.network_address==ip_address("175.184.48.0"):
        print(mask)