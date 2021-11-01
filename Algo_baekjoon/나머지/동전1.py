N, K = map(int, input().split())
coins = []
for n in range(N):
    coins.append(int(input()))

dp = [0] * (K+1)
dp[0] = 1

for c in coins:
    for n in range(1, K+1):
        if n >= c:
            dp[n] += dp[n-c]
    print(dp)
print(dp[K])
