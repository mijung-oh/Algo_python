T = int(input())
# x는 행, y는 열
# 상 우 하 좌 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, BRD, visited):
    if BRD[x][y] == '3':
        return True
    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]
        if 0<=newX<len(BRD) and 0<=newY<len(BRD) and BRD[newX][newY] != '1' and visited[newX][newY] == 0:
            visited[newX][newY] = 1
            if dfs(newX, newY, BRD, visited):
                return True
    return False

for tc in range(1, T+1):
    N = int(input())
    BRD = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        BRD.append(list(input()))

    check = 0
    for i in range(len(BRD)):
        for j in range(len(BRD[i])):
            if BRD[i][j] == '2':
                visited[i][j] = 1
                check = 1
                if dfs(i, j, BRD, visited):
                    print('#{} {}'.format(tc, 1))
                else:
                    print('#{} {}'.format(tc, 0))
                break
        if check:
            break

