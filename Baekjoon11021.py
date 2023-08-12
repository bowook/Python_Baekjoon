import sys
testCase = int(input())

for i in range(1, testCase+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i, a+b))