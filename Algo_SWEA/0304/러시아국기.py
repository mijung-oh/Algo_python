T = int(input())

# 0 1 2 3
# W W W R
# W W B R
# W B B R
# W B R R
# preC가 W이면 선택권은 W, B
WB = ['W', 'B']
# preC가 B이면 선택권은 B, R
BR = ['B', 'R']
def dfs(preC, r, count):
    global min_count
    # 만약 마지막행인데 preC가 W이면 False 리턴
    if r == N-1 and preC == 'W':
        return False
    elif (r==N-1 and preC == 'B') or (r==N-1 and preC == 'R'):
        return count
    pre_count = count

    if preC == 'W':
        for i in WB: # i는 W, B
            count = pre_count
            # 개수 세주기
            for j in range(M):
                if BRD[r][j] != i:
                    count += 1
            preC = i
            c = dfs(preC, r+1, count)

            if c and min_count > c:
                min_count = c

    elif preC == 'B':
        for i in BR: # i는 B, R
            # 개수 세주기
            count = pre_count
            for j in range(M):
                if BRD[r][j] != i:
                    count += 1
            preC = i
            c = dfs(preC, r + 1, count)
            if c and min_count > c:
                min_count = c
    elif preC == 'R':
        count = pre_count
        for j in range(M):
            if BRD[r][j] != 'R':
                count += 1
        preC = 'R'
        c = dfs(preC, r + 1, count)
        if c and min_count > c:
            min_count = c

    return min_count



for tc in range(1, T+1):
    #N행 M열
    N, M = map(int, input().split())
    BRD = []
    for n in range(N):
        BRD.append(list(input()))
    min_count = 1000000
    cnt = 0
    # 전 행의 색깔
    preC = ''
    #첫줄은 무조건 whilte, 마지막줄은 무조건 red
    for n in range(N):
        # 첫줄일경우
        if n == 0:
            preC = 'W'
            for k in range(M):
                if BRD[n][k] != 'W':
                    BRD[n][k] = 'W'
                    cnt += 1
        # 마지막줄인경우 모두 레드로
        elif n == N-1:
            for k in range(M):
                if BRD[n][k] != 'R':
                    BRD[n][k] = 'R'
                    cnt += 1
    a = dfs(preC, 1, 0)
    cnt += a

    print('#{} {}'.format(tc, cnt))

