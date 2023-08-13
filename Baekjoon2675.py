testCase = int(input())

for i in range(0, testCase):
    a, b = input().split()
    a = int(a)
    b = str(b)
    for j in range(0, len(b)):
        print(b[j] * a, end='')
    print()
