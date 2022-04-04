N = int(input())
stairs = [0]
for n in range(N): stairs.append(int(input()))
# dp[i] = i 번째 계단까지 점수
dp = [[0, 0] for _ in range(N+1)]
# 마지막 계단

for i in range(1, N+1):
    # 마지막 계단일 경우
    if i == N:
        if dp[i-1][1] < 2:
            dp[i][0] = max(dp[i][0], max(dp[i-1][0]+stairs[i], dp[i-2][0]+stairs[i]))
        else:
            dp[i][0] =dp[i-2][0]+stairs[i]
    else:
        # 바로 전 계단에서 올 경우
        if dp[i-1][1] < 2 and dp[i][0] < dp[i-1][0] + stairs[i]:
            dp[i][0] = dp[i-1][0] + stairs[i]
            dp[i][1] = dp[i-1][1] + 1
        else:
            dp[i-1][1] = 0

        # 전전 단계에서 올 경우
        if i > 1 and dp[i][0] < dp[i-2][0] + stairs[i]:
            dp[i][0] = dp[i-2][0] + stairs[i]
            dp[i][1] = 1
    print(dp)
print(dp[N][0])