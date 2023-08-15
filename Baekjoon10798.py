metrix = [['*' for i in range(0, 15)] for j in range(0,15)]

for i in range(0, 5):
    word = list(input())
    for j in range(0, len(word)):
        metrix[i][j] = word[j]
    

for i in range(0, 15):
    for j in range(0, 15):
        if(metrix[j][i] != '*'):
            print(metrix[j][i], end='')
        