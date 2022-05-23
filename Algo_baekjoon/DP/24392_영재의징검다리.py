N, M = map(int, input().split())
MOD = 1000000007
BRD = []

# dp[i][j] = (i,j) 에서 끝 행까지 갈 수 있는 경우의수
dp = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    BRD.append(list(map(int, input().split())))

# 첫 번째 행 업데이트
for i in range(M):
    if BRD[0][i]:
        dp[0][i] = 1

# dp 업데이트
for r in range(1, N):
    for c in range(M):
        if BRD[r][c]:
            cnt = 0
            if 0 <= c-1 and dp[r-1][c-1]:
                cnt += dp[r-1][c-1] % MOD
            if c+1 < M and dp[r-1][c+1]:
                cnt += dp[r-1][c+1] % MOD
            if dp[r-1][c]:
                cnt += dp[r-1][c] % MOD
            dp[r][c] = cnt % MOD

print(sum(dp[N-1]) % MOD)

