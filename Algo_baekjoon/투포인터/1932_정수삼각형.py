N = int(input())
graph = [[] for _ in range(N)]

# n층까지의 부분합
dp = [[0 for _ in range(N)] for _ in range(N)]

for n in range(N):
    graph[n] = list((map(int, input().split())))
    
dp[0][0] = graph[0][0]
for i in range(len(graph)-1):
    for j in range(len(graph[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + graph[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + graph[i+1][j+1])

print(max(dp[N-1]))