from ipaddress import ip_network
net=ip_network("158.214.121.40/255.255.255.224",strict=False)
for ip in net:
    print(ip)
print(net.broadcast_address, net.network_address)