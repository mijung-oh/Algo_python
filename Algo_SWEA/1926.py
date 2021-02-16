N = int(input())

def isThree(n):
    count = 0
    while n:
        tg = n % 10
        # 한 자리수가 3의 배수이면(3 or 6 or 9)
        if tg != 0 and tg % 3 == 0:
            count += 1
        n //= 10

    return count

for n in range(1, N+1):
    cnt = isThree(n)
    if cnt == 0:
        print(n, end=' ')
    else:
        while cnt:
            print('-', end='')
            cnt -= 1
        print('', end=' ')