starCount = int(input())

for i in range(1, starCount +1):
    for j in range(starCount, i, -1):
        print(' ', end='')
    for k in range(0, i):
        print('*', end='')
    print()