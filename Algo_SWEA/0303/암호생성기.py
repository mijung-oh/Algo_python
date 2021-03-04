for t in range(1, 11):
    tc = int(input())
    q = list(map(int, input().split()))

    check = 0
    while 1:
        for i in range(1, 6):
            front = q.pop(0)
            if front-i <= 0:
                q.append(0)
                check = 1
                break
            q.append(front-i)
        if check:
            break
    print('#{}'.format(tc), end=' ')
    print(*q)