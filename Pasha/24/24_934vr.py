file = open('ItEge/Pasha/24/24_934.txt').readline()
start = 0
end = 1
alph = set()
mx_len = 0
second = 0
while start != len(file) - 1:
    if file[end]==file[end-1]:
        end+=1
    else:
        if file[end]>file[end-1]:
            alph.add(file[end])
            if len(alph) == 2:
                second = end
            if len(alph) == 3:
                mx_len = max(mx_len, end - start)
            elif len(alph) == 4:
                mx_len = max(mx_len, end - start - 1)
                alph.remove(file[start])
                start = second
        else:
            if len(alph) == 3:
                mx_len = max(mx_len, end - start)
            else:
                start = end
                alph = set(file[end])
        end+=1