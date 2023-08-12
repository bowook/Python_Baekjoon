remain_num = []
for i in range(0, 10):
    num = int(input())

    if(num % 42 not in remain_num):
        remain_num.append(num % 42)

print(len(remain_num))



