N, K = map(int, input().split())
lst = [(0,0)]
for n in range(N):
    w, v = map(int, input().split())
    lst.append((w, v))

# dp[i][j] => i 아이템의 j 무게일 때 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# i번째 아이템에서
for i in range(1, N+1):
    # 무게가 j
    for j in range(1, K+1):
        if j < lst[i][0]:
            dp[i][j] = dp[i-1][j]
            continue
        # 현재 i 아이템을 가져가지 않을 경우: dp[i-1][j]
        # 현재 i 아이템을 가져갈 경우: dp[i-1][]
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][0]] + lst[i][1])

for i in range(N+1):
    print(*dp[i])
print(dp[N][K])