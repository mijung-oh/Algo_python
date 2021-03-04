T = int(input())
# 방향 상 하 좌 우
# x는 행 y는 열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
def bfs(x,y, visited):
    q.append((x,y))
    while q:
        new = q.pop(0)
        newX = new[0]
        newY = new[1]
        for i in range(4):
            if 0<= newX+dx[i] <N and 0 <= newY+dy[i] < N and visited[newX+dx[i]][newY+dy[i]] == 0 and BRD[newX+dx[i]][newY+dy[i]] != 1:
                q.append((newX+dx[i], newY+dy[i]))
                visited[newX+dx[i]][newY+dy[i]] = visited[newX][newY]+1
    return visited

for tc in range(1, T+1):
    N = int(input())
    BRD = []
    # BRD 입력 받기
    for i in range(N):
        BRD.append(list(map(int, input())))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 시작지점 찾기
    x = y = 0
    for i in range(N):
        for j in range(N):
            # 시작지점 찾으면 bfs 실행
            if BRD[i][j] == 2:
                visited = bfs(i,j, visited)
                print(visited)

    for i in range(N):
        for j in range(N):
            if BRD[i][j] == 3:
                if visited[i][j] == 0:
                    print('#{} {}'.format(tc, visited[i][j]))
                    break
                print('#{} {}'.format(tc, visited[i][j]-1))
                break