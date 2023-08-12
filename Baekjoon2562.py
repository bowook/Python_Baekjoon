num_list = [0] * 9

for i in range(0, 9):
    num_list[i] = int(input())

print(max(num_list))
print(num_list.index(max(num_list))+1)
