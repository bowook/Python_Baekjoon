nineByNineMetrix = [[0 for i in range(9)] for j in range(9)]

for i in range(0,9):
    nineByNineMetrix[i] = list(map(int,input().split()))
max_metrix : int = 0
row : int = 0
colum : int = 0
for i in range(0, 9):
    for j in range(0, 9):
        if(nineByNineMetrix[i][j]>max_metrix):
            max_metrix = nineByNineMetrix[i][j]
            row = i
            colum = j

print(max_metrix)
print(row+1, colum+1, end=' ')
