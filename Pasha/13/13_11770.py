from ipaddress import *
ip = ip_address('251.211.38.240')
net = ip_address('251.211.38.0')
cnt = 0
for mask in range(0, 33):
    network = ip_network(f'{ip}/{mask}',0)
    if net == network.network_address:
        cnt += 1
print(cnt)
