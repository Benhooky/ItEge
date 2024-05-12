from ipaddress import *
ip1= f'{ip_address('112.117.107.70'):b}'
ip2= f'{ip_address('112.117.121.80'):b}'
s=''
for i in range(16,24):
    if ip1[i]==ip2[i]:
        s+='1'
    else:
        break
if len(s)!=8:
    s=s+'0'*(8-len(s))
print(int(s,2))