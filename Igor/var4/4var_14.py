from string import digits, ascii_uppercase
alphadet=(digits+ascii_uppercase)[:19]
listansw=[]
for x in alphadet:
    sum1 = int(f"3{x}2{x}1{x}0{x}1",19) + int(f"{x}2024",19) + int(f"1{x}077",19)
    if sum1%18==0:
        listansw.append(sum1/18)
print(max(listansw))