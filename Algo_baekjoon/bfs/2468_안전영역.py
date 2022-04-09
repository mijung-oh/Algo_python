import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
heights = set()
heights.add(0)
BRD = []

for i in range(N):
    t = list(map(int, input().split()))
    # 높이를 set에 저장
    heights.update(t)
    BRD.append(t)

def bfs(h):
    global N
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    # h 이하인 지역들은 visited 1표시
    for i in range(N):
        for j in range(N):
            if BRD[i][j] <= h: 
                visited[i][j] = 1

    for i in range(N):
        for j in range(N):
            # h 보다 높은 지역인 경우
            if not visited[i][j]:
                q = deque()
                q.append((i,j))
                cnt += 1
                while q:
                    r, c = q.popleft()
                    for d in [(1, 0), (0,1), (-1,0), (0,-1)]:
                        nr = r + d[0]
                        nc = c + d[1]
                        # h보다 높은 지역인 경우
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
    return cnt
                
result = -1

for h in heights:
    # 영역 개수의 최댓값 저장
    result = max(result, bfs(h))
print(result)