from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
# graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
# i번의 부모
parent = [0] * (N+1)
parent[1] = 1

for n in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for g in graph[cur]:
        if g and not parent[g]:
            parent[g] = cur
            q.append(g)

for i in range(2, len(parent)):
    print(parent[i])