from collections import deque
T = int(input())
# 방향은 오른쪽, 아래
# x는 행, y는 열
dx = [0, 1]
dy = [1, 0]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        new = q.popleft()
        for i in range(2):
            newX = new[0]+dx[i]
            newY = new[1]+dy[i]
            if 0<=newX<N and 0<=newY<N and BRD[newX][newY] != 0 and visited[newX][newY] == 0:
                q.append((newX,newY))
                visited[newX][newY] = 1
    # 열 개수 c
    c = 0
    for i in range(y, N):
        if visited[x][i] == 1:
            c += 1
        else:
            break
    r = 0
    for i in range(x, N):
        if visited[i][y] == 1:
            r += 1
        else:
            break
    return (r,c)




for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))

    visited = [[0 for x in range(N)] for y in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and BRD[i][j]!=0:
                r,c = bfs(i,j)
                result.append((r*c, r, c))
    print('#{} {}'.format(tc, len(result)), end=' ')
    result = sorted(result)
    for i in range(len(result)):
        print('{} {}'.format(result[i][1], result[i][2]), end=' ')
    print()