num_list = list(input().split())

for i in range(0, 2):
    num_list[i] = num_list[i][::-1]

print(max(num_list))
