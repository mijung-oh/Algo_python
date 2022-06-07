N = int(input())

dp = [100000 for _ in range(N+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
# 제곱수 초기화
idx = 1
while idx * idx <= N:
    dp[idx* idx] = 1
    idx += 1

for i in range(4, N+1):
    # dp 초기화
    for j in range(i-1, i//2, -1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])
print(dp[N])