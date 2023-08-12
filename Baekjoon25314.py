byte_num = int(input())
#byte_num은 무조건 4의 배수
#4일 경우 long int
#8일 경우 long long int
cnt = byte_num // 4

for i in range(0,cnt):
    print('long', end=' ')

    if(i == cnt-1) :
        print('int')