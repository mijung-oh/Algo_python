import sys
input = sys.stdin.readline

N = int(input())
T, P = [0], [0]

for n in range(N):
    t, p = map(int, input().split())
    T.append(t); P.append(p)

# i번째 까지 최대 금액
dp = [0] * (N+2)

for i in range(1, N+1):
    # 상담이 끝난 후 금액
    if i + T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    # 상담을 진행하지 않을 경우
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N+1])