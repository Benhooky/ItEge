from string import digits,ascii_uppercase
for x in (digits+ascii_uppercase)[:27]:
    s = int(f'17{x}35',27) + int(f"{x}742M",27) + int(f"{x}",27)**3
    if s%23==0:
        print(s//23)