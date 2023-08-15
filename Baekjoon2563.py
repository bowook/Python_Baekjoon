metrix = [[0 for i in range(0, 100)] for j in range(0, 100)]
paper_num = int(input())
#색종이의 길이는 10 고정이야 정사각형
sum : int = 0
for i in range(0, paper_num):
    x, y = map(int, input().split())
    #입력받는 a,b는 색종이의 왼쪽아래 모서리
    for j in range(x-1, x+9):
        #2번 인덱스부터 11번 인덱스까지 채움, 밑변
        for k in range(y-1, y+9):
            #6번 인덱스부터 15번 인덱스까지 채움 높이
            metrix[j][k] = 1


for i in range(0, 100):
    for j in range(0, 100):
        if(metrix[i][j] == 1):
            sum+=1
        else:
            continue
print(sum)
        



