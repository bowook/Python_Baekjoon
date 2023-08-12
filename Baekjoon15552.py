import sys
testCase = int(input())
for i in range(0, testCase):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)