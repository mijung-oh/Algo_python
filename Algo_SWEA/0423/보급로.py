from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global N
    dq = deque()
    dq.append((r, c))
    while dq:
        sr, sc = dq.popleft()
        for i, j in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            nr = sr + i
            nc = sc + j
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[sr][sc] + int(BRD[nr][nc]):
                    dist[nr][nc] = dist[sr][sc] + int(BRD[nr][nc])
                    dq.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    BRD = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dist = [[0xffff for _ in range(N)] for _ in range(N)]

    dist[0][0] = 0
    bfs(0,0)
    # for i in range(N):
    #     print(*dist[i])
    print(dist[N-1][N-1])

