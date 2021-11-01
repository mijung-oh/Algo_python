T = int(input())
from collections import deque
# q = []
# 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[stX][stY] = 1
    q = deque([(stX,stY)])
    while q:
        newX, newY = q.popleft()
        if newX == enX and newY == enY:
            return visited[newX][newY]

        for i in range(8):
            if 0<= newX+dx[i] <N and 0<= newY+dy[i] < N and visited[newX+dx[i]][newY+dy[i]] == 0:
                visited[newX + dx[i]][newY + dy[i]] = visited[newX][newY] + 1
                q.append((newX+dx[i], newY+dy[i]))
    return visited


for tc in range(1, T+1):
    N = int(input())

    stX, stY = map(int, input().split())
    enX, enY = map(int, input().split())

    print(bfs()-1)