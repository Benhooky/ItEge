from itertools import permutations 
f=permutations("ПАРИЖАНКА",9)
lst=[]
for x in f:
    lst.append("".join(x))
cnt=0
for word in set(lst):
    if "ААА" not in word:
        if word.count("АА") + word.count("АИ") + word.count("ИИ") + word.count("ИА")==1:
            cnt+=1
            print(word)
print(cnt)