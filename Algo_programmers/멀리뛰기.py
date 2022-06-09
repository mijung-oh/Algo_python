def solution(n):
    answer = 0
    # # dp[i]: i번째까지 도달할 수 있는 횟수
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 1 1 1/ 1 2/ 21 = 3
    # dp[4] = 1 1 1 1, 22, 112, 211, 121 = 5
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

solution(4)