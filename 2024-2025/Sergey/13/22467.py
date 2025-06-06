from ipaddress import ip_network
cnt=0
for mask in range(0,33):
    net=ip_network(f"192.214.116.184/{mask}",strict=False)
    binIp=f"{net.network_address:b}"
    if binIp.count("1")%5==0:
        cnt+=1
        print(net.network_address)
print(cnt)