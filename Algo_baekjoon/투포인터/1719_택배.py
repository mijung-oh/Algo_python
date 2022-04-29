import sys

from flask import g
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
road = [[0 for _ in range(N+1)] for _ in range(N+1)]

for m in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    road[a][b] = b
    road[b][a] = a

# 자기 자신에게는 0
for i in range(1, N+1):
    graph[i][i] = 0

# 거쳐가는 점
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                road[i][j] = road[i][k]
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            print("-", end=" ")
        else:
            print(road[i][j], end=" ")
    print()