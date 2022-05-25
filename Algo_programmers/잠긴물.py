from collections import deque
MOD = 1000000007

def solution(m, n, puddles):
    answer = 0
    # mxn
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # 잠긴 곳 체크
    for p in puddles:
        dp[p[1]][p[0]] = -1

    dp[1][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:
                continue
            total = 0
            if dp[i-1][j] != -1: total += dp[i-1][j]
            if dp[i][j-1] != -1: total += dp[i][j-1]

            dp[i][j] = total % MOD
    for i in range(len(dp)):
        print(*dp[i])
    print(dp[n][m])

    
    return answer
solution(4, 3, [[2, 2]])