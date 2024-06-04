from ipaddress import *
listAns = []
for mask in range(33):
    net = ip_network(f"192.75.64.98/{mask}",strict=False)
    cnt=0
    if ip_address('192.75.64.0') in net:
        listAns.append(32-mask)
print(min(listAns))