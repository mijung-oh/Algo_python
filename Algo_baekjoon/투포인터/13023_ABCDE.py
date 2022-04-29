import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * N

def dfs(cur_node, cnt):
    if cnt == 4:
        return True
    # 현재 노드로부터 연결된 노드로 탐색
    for i in graph[cur_node]:
        if not visited[i]:
            visited[i] = 1
            if dfs(i, cnt+1): return True
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    if dfs(i, 0):
        print(1)
        exit()
    visited[i] = 0
print(0)