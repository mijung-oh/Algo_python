from collections import deque

# N, M = 세로, 가로
R, C = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(R)]
time = 0

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0] * C for _ in range(R)]
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if BRD[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                else:
                    BRD[nr][nc] += 1
while 1:
    # 값이 3 이상인 것들이 곧 녹을 치즈이므로 0으로 초기화한다.
    check = False
    visited = [[0] * C for _ in range(R)]
    bfs()
    print()
    for i in range(len(BRD)):
        print(*BRD[i])
    for r in range(R):
        for c in range(C):
            if BRD[r][c] >= 3:
                check = True
                BRD[r][c] = 0
            # 만약 BRD값이 2이면 다시 bfs를 돌 때 초기상태로 돌아야하므로
            elif BRD[r][c] == 2: # 한 면만 접촉해있는 상태이므로
                BRD[r][c] = 1
    if check:
        time += 1
    else:
        break
print(time)
