mas=[int(x) for x in open("ItEge/2024-2025/Sergey/17/17_7682.txt")]
cnt3=0
cnt4=0
max570=max(abs(x) for x in mas if abs(x)%570==0)

for i in range(len(mas)-3):
    quart = [mas[i], mas[i+1], mas[i+2], mas[i+3]]
    if sum(quart)/4>max570:
        cnt4+=1

for i in range(len(mas)-2):
    quart = [mas[i], mas[i+1], mas[i+2]]
    if sum(quart)%34==0: 
        if sum(1 for x in quart if x>0)>=2:
            cnt3+=1
print(cnt4,cnt3)