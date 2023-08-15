def transNotation(num, n):
    #10진수 num, N진수 n
    result = []

    if num == 0:
        result.append(0)

    while num > 0:
        #10진수 num을 n진수로 나눈 나머지를 문자열형태로 더함
        if num % n < 10:
            result.append(num % n)
        else:
            result.append(chr(num % n - 10 + ord('A')))
        num //= n
        #num값을 n으로 나누어 갱신하는것을 num이 0이 될 때까지 반복

    return result[::-1]

a, b = map(int,input().split())
c = transNotation(a,b)

for i in range(0,len(c)):
    print(c[i], end='')
