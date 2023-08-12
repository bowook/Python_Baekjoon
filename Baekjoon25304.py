csm_money_sum = int(input())
buy_item_cnt = int(input())
sum = 0
for i in range(0, buy_item_cnt):
    csm_money, item_cnt = map(int,input().split())

    sum += csm_money * item_cnt

if(sum == csm_money_sum):
    print('Yes')
else:
    print('No')