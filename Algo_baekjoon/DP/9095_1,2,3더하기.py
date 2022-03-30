T = int(input())

dp = [0] * 101
dp[1] = 1 # 1 = 1
dp[2] = 2 # 2 = 1+1, 2
dp[3] = 4 # 3 = 1+1+1, 1+2, 2+1, 3

for t in range(T):
    n = int(input())
    # dp 배열 채우기
    i = 2
    while i <= n:
        if dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        i += 1
    print(dp[n])