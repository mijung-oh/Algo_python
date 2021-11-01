import sys
input = sys.stdin.readline
N = int(input())

cost = []
for n in range(N):
    cost.append(list(map(int, input().split())))

# 0: red, 1: green, 2: blue
dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = cost[0]

for n in range(1, N):
    dp[n][0] = min(cost[n][0] + dp[n-1][1], cost[n][0] + dp[n-1][2])
    dp[n][1] = min(cost[n][1] + dp[n-1][0], cost[n][1] + dp[n-1][2])
    dp[n][2] = min(cost[n][2] + dp[n-1][0], cost[n][2] + dp[n-1][1])

print(min(dp[N-1]))