N, standard_num  = map(int, input().split())
number_list = list(map(int, input().split()))
for i in range(0, N):
    if(number_list[i] < standard_num):
        print(number_list[i], end=' ')