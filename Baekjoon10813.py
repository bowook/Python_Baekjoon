N, M = map(int, input().split())
basket = [0] * N
for i in range(0, N):
    basket[i] = i+1

for i in range(0, M):
    a, b = map(int, input().split())
    temp = basket[a-1]
    basket[a-1] = basket[b-1]
    basket[b-1] = temp

for i in range(0, N):
    print(basket[i], end=' ')