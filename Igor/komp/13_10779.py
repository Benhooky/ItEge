from ipaddress import *
listAns = []
for mask in range(33):
    net = ip_network(f"111.91.192.0/{mask}",strict=False)
    cnt=0
    if ip_address('111.91.200.28') in net:
        listAns.append(32-mask)
print(min(listAns))
