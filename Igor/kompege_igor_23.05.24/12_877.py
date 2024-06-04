lst=[]
answerN=0
mincount1=10000
for n in range(100,1000):
    s= "1"*n
    while "111" in s:
        s=s.replace("111","2",1)
        s=s.replace("2222","333",1)
        s=s.replace("33","1",1)
    if s.count("1") < mincount1:
        mincount1=s.count("1")
        answerN=n
print(answerN)