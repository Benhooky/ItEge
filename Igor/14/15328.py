from string import digits, ascii_uppercase
alphabet=(digits+ascii_uppercase)[:27]
listansw=[]
for x in alphabet:
    sum1 = int(f"123{x}24",27) + int(f"135{x}78",27)
    if sum1%26==0:
        listansw.append(sum1/26)
print(max(listansw))