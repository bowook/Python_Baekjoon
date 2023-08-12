std_number = [0] * 30

for i in range(0, 30):
    a = int(input())

    std_number[a-1] = a

    if(i == 27) :
        break

count : int = 0
for i in range(0, 30):
    if(std_number[i] == 0) :
        print(i+1)
        count+=1
    if(count == 2):
        break
    