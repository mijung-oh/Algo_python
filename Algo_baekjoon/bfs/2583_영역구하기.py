from locale import currency
import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

BRD = [[0] *M for _ in range(N)]

def bfs(r, c):
    global M, N
    q = deque()
    q.append((r,c))
    while q:
        cur_r, cur_c = q.popleft()
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr, nc = cur_r + d[0], cur_c + d[1]
            if 0 <= nr < N and 0 <= nc < M and not BRD[nr][nc]:
                BRD[nr][nc] = 1
                q.append((nr, nc))


# 영역 칠하기
for k in range(K):
    r, c, rr, cc = map(int, input().split())
    for i in range(r, rr):
        for j in range(c, cc):
            if not BRD[i][j]:
                BRD[i][j] = 1

count = 0
# 영역 구하기
for i in range(N):
    for j in range(M):
        if not BRD[i][j]:
            bfs(i, j)
            count += 1
print(count)