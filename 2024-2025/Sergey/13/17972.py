from ipaddress import ip_network
net= ip_network("123.222.111.192/255.255.255.248",strict=False )
cnt=0
for ip in net:
    binip=f"{ip:b}"
    if binip[-8:].count("0")%3!=0:
        cnt+=1
print(cnt)