from string import digits, ascii_uppercase
for x in (digits+ascii_uppercase)[:32]:
    value = int(f'931{x}964',32)+int(f'4{x}51{x}1',32)+int(f'2861{x}637',32)
    if value%31==0:
        print(value/31)
        break