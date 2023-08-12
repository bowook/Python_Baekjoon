str_arr = input()
apb = []
ascNum = 97
for i in range(0, 26):
    apb.append(chr(ascNum))
    ascNum+=1

for i in range(0, 26):
    if(apb[i] in str_arr):
        apb[i] = str_arr.index(apb[i])
    else:
        apb[i] = -1
    print(apb[i], end=' ')