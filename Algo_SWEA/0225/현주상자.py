T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lst = [0]*(N+1)
    for q in range(1, Q+1):
        l, r = map(int, input().split())
        for i in range(l, r+1):
            lst[i] = q

    print('#{}'.format(tc), end=' ')
    print(*lst[1:], end=' ')
    print()