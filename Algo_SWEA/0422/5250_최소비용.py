from collections import deque
dr = [-1,1, 0, 0]
dc = [0,0, -1, 1]

T = int(input())

def bfs(current):
    global N
    dq = deque()
    dq.append(current)
    while dq:
        go = dq.popleft()
        # print(dq)
        for i in range(4):
            nr = go[0] + dr[i]
            nc = go[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 가려는 곳이 더 높은 위치이면서 dist가 더 큰 경우
                if BRD[nr][nc] > BRD[go[0]][go[1]]:
                    if dist[nr][nc] > dist[go[0]][go[1]] + 1 + (BRD[nr][nc] - BRD[go[0]][go[1]]):
                        dist[nr][nc] = dist[go[0]][go[1]] + 1 + (BRD[nr][nc] - BRD[go[0]][go[1]])
                        dq.append((nr, nc))
                else:
                    if dist[nr][nc] > dist[go[0]][go[1]] + 1:
                        dist[nr][nc] = dist[go[0]][go[1]] + 1
                        dq.append((nr, nc))
                
    
    

for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for n in range(N)]
    dist = [[0xffff for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    bfs((0,0))
    # print()
    # for i in range(N):
    #     print(*dist[i])
    print('#{} {}'.format(tc, dist[N-1][N-1]))
