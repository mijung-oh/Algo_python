T = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for t in range(T):
    n = int(input())
    # dp 배열 채우기
    i = 2
    while i <= n:
        if dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        i += 1
    print(dp[n])