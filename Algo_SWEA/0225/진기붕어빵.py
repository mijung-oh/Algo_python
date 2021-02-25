T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int , input().split())
    mkBoong = [0]*11112
    coming = [0]*11112

    # 사람 오는 시간
    person = list(map(int, input().split()))
    person.sort()

    #붕어빵 만들기
    for i in range(0, len(mkBoong), M):
        mkBoong[i] = K
    check = 1
    min_idx = M
    for p in person:
        if min_idx <= p and mkBoong[min_idx]:
            mkBoong[min_idx] -= 1
            if mkBoong[min_idx] == 0:
                min_idx += M
        else:
            check = 0
            break
    if check:
        print('#{} {}'.format(tc, 'Possible'))
    else:
        print('#{} {}'.format(tc, 'Impossible'))



