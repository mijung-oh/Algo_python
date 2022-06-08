N = int(input())
if N <= 3:
    print(N)
    exit()

dp = [100000 for _ in range(N+1)]

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, N+1):
    # 이전 값에 1을 더한 값과 같으므로
    dp[i] = dp[i-1] + 1
    j = 1
    while j*j <= i:
        if dp[i-j*j]+ d[j*j] < dp[i]:
            dp[i] = dp[i-j*j]+1
        j += 1
print(*dp)
print(dp[N])