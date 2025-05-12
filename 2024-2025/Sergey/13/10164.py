from ipaddress import ip_network,ip_address
net=ip_network("156.132.15.138/255.255.252.0",strict=False)
num=0
for ip in net:
    num+=1
    if ip==ip_address('156.132.15.138'):
        print(num-1)