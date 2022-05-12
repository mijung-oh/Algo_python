
from collections import deque

def bfs(v, dist, adj):
    q = deque()
    q.append(v)
    while q:
        cur_node = q.popleft()
        for e in adj[cur_node]:
            if dist[e] == -1:
                dist[e] = dist[cur_node]+1
                q.append(e)
    return dist

def solution(n, edge):
    answer = 0
    dist = [-1] * (n+1)
    
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    dist[1] = 0
    dist = bfs(1, dist, adj)
    return answer
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)