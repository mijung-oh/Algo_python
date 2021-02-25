T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    # 거꾸로 돌면서 작을때만 이자 더해준다.
    max = cost[-1]
    total = 0
    for i in range(len(cost)-2, -1, -1):
        if max > cost[i]:
            total += max - cost[i]
        else:
            max = cost[i]

    print('#{} {}'.format(tc, total))
