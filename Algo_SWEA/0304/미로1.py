from collections import deque
# x는 행 y는 열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((stX, stY))
    while q:
        new = q.popleft()

        for i in range(4):
            newX = new[0] + dx[i]
            newY = new[1] + dy[i]
            if newX == enX and newY == enY:
                return 1
            if 0<= newX < 16 and 0<= newY < 16 and visited[newX][newY] == 0\
                    and BRD[newX][newY] == 0:
                visited[newX][newY] = 1
                q.append((newX, newY))
    return 0

for t in range(1, 11):
    tc = int(input())
    BRD = []
    for i in range(16):
        BRD.append(list(map(int, input())))
    visited = [[0 for x in range(16)] for y in range(16)]
    for i in range(16):
        for j in range(16):
            if BRD[i][j] == 2:
                stX, stY = i, j
            elif BRD[i][j] == 3:
                enX, enY = i, j
    print('#{} {}'.format(tc, bfs()))