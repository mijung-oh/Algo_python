from glob import glob
from re import L


N, M = map(int, input().split())
graph = [[-1] * (N+1) for _ in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

def dijk(cur_node, dist):
    global N
    for node in range(1, N+1):
        if graph[cur_node][node] and dist[node] == -1:
            dist[node] = dist[cur_node] + graph[cur_node][node]
            dijk(node, dist)
    return dist

for st in range(1, N+1):
    graph[st][st] = 0
    d = dijk(st, graph[st])
    print(d)
    graph[st] = d

for i in range(N+1):
    print(*graph[i])