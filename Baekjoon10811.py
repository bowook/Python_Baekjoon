N, M = map(int, input().split())

num_list = [0] * N

for i in range(0, len(num_list)):
    num_list[i] = i+1

for i in range(0, M):
    a, b = map(int, input().split())
    num_list[a-1:b] = reversed(num_list[a-1:b])

for i in range(0, N):
    print(num_list[i], end=' ')