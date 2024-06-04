from ipaddress import *
listA=[]
for A in range(16,25):
    net = ip_network(f"152.65.245.132/{A}",strict=False)
    if all(f"{ip:b}"[:16].count("0")>=f"{ip:b}"[16:].count("0") for ip in net):
        listA.append(A)
print(min(listA))