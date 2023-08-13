# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

chess_list = list(map(int, input().split()))

standard_chess_list = [1, 1, 2, 2, 2, 8]

for i in range(0, len(chess_list)):
    flag = True
    if(chess_list[i] > standard_chess_list[i]):
        while flag:
            minus = chess_list[i] - standard_chess_list[i]
            chess_list[i] = -minus
            flag = False
    elif(chess_list[i] < standard_chess_list[i]):
        while flag:
            plus = standard_chess_list[i] - chess_list[i]
            chess_list[i] = plus
            flag = False
    else:
        chess_list[i] = 0

for i in range(0, len(chess_list)):
    print(chess_list[i], end=' ')
            
        
