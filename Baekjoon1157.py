input_str = input().upper()
set_input_str = list(set(input_str))
cnt_list = []

for i in set_input_str:
    cnt = input_str.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(set_input_str[max_index])
