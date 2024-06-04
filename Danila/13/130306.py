from ipaddress import ip_network
for mask in range(16,25):
    net = ip_network(f"127.63.67.1/{mask}",strict=False)
    if all(f'{ip:b}'[:16].count('1')>=f'{ip:b}'[16:].count('1') for ip in net):
        print(mask)
print(int('11110000',2))