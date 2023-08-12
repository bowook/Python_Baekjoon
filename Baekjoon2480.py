dice_num = list(map(int, input().split()))

if(dice_num.count(dice_num[0]) == 3) :
    #다 같을때니까 상관없고
    print(10000 + dice_num[0] * 1000)
elif(dice_num.count(dice_num[0]) == 2) :
    print(1000 + dice_num[0] * 100)
elif(dice_num.count(dice_num[0]) == 1):
    if(dice_num.count(dice_num[1]) == 1) :
        print(max(dice_num) * 100)
    elif(dice_num.count(dice_num[1]) == 2):
        print(1000 + dice_num[1] * 100)