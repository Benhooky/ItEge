from ipaddress import ip_network
net= ip_network("1/255.240.0.0",strict=False )
cnt=0
for ip in net:
    binip=f"{ip:b}"
    if binip.count("1")%5==0:
        cnt+=1
print(cnt)