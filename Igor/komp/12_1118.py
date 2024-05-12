for n in range(0,100):
    for i in range(0,100):        
        for j in range(0,100):
            s = "0" + "1"*n + "2"*i + "3"*j
            while "01" in s or "02" in s or "03" in s:
                s=s.replace("01","302",1)
                s=s.replace("02","3103",1)
                s=s.replace("03","20",1)
            if s.count("1")==28 and s.count("2")==34 and s.count("3")==45:
                print(n)
                break