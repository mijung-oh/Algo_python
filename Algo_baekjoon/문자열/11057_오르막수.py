N = int(input())

# dp[수의 길이][시작 숫자]
dp = [[0 for _ in range(10)] for _ in range(N+1)]
# 한 자리일 때
for i in range(10):
    dp[1][i] = 1

# 두 자리 이상일 때
for i in range(2, N+1):
    # 시작 숫자
    for j in range(10):
        s = 0
        for k in range(j, 10):
            s += dp[i-1][k]
        dp[i][j] = s % 10007
print(sum(dp[N]) % 10007)