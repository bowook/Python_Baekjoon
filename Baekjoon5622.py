str_arr = input()
time : int = 0
for i in range(0, len(str_arr)):
    if str_arr[i] == 'A' or str_arr[i] =='B' or str_arr[i] == 'C':
        time += 3
    elif str_arr[i] == 'D' or str_arr[i] =='E' or str_arr[i] =='F':
        time += 4
    elif str_arr[i] == 'G' or str_arr[i] =='H' or str_arr[i] =='I':
        time += 5
    elif str_arr[i] == 'J' or str_arr[i] =='K' or str_arr[i] =='L':
        time += 6
    elif str_arr[i] == 'M' or str_arr[i] =='N' or str_arr[i] =='O':
        time += 7
    elif str_arr[i] == 'P' or str_arr[i] =='Q' or str_arr[i] =='R' or str_arr[i] =='S':
        time += 8
    elif str_arr[i] == 'T' or str_arr[i] =='U' or str_arr[i] =='V':
        time += 9
    elif str_arr[i] == 'W' or str_arr[i] =='X' or str_arr[i] =='Y' or str_arr[i] =='Z':
        time += 10

print(time)
