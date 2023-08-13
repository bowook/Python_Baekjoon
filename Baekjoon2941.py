input_arr = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    input_arr = input_arr.replace(i, '!')
print(len(input_arr))