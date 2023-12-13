from ipaddress import *

ip = ip_address("157.17.164.129")
net = ip_address("157.17.128.0")
for mask in range(16, 33):
    network = ip_network(f"{ip}/{mask}", 0)
    if net == network.network_address:
        print(network.netmask)
        break
