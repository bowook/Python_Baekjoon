N, M = map(int, input().split())
#N은 행, M은 열
first_metrix = [[0 for i in range(M)] for j in range(N)]
second_metrix = [[0 for i in range(M)] for j in range(N)]
# 1 1 1   3 3 3   4 4 4
# 2 2 2   4 4 4   6 6 63
# 0 1 0   5 5 100 5 6 100

metrix = []
for i in range(0,N): #N은 행
    metrix = list(map(int, input().split()))
    for j in range(0, M):
        first_metrix[i][j] = metrix[j]

for i in range(0, N):
    metrix = list(map(int, input().split()))
    for j in range(0, M):
        second_metrix[i][j] = metrix[j]

for i in range(0, N):
    for j in range(0, M):
        first_metrix[i][j] += second_metrix[i][j]

for i in range(0, N):
    for j in range(0, M):
        print(first_metrix[i][j], end=' ')
    print()