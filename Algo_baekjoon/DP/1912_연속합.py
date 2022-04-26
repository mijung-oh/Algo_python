import sys

N = int(input())
numbers = list(map(int, input().split()))

# i번째까지 연속된 합 중 최대값
dp = [0] * N
dp[0] = numbers[0]

for i in range(N):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])
print(max(dp))