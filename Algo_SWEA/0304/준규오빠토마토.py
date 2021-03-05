from collections import deque
from sys import stdin

def start(farm):
    se = []
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                se.append([i, j])
    return se

def safe(x, y):
    if (x >= m or x < 0 or y >= n or y < 0):
        return False
    else:
        if farm[x][y] == -1:
            return False
        else:
            return True

def BFS(x, y):
    global farm
    queue = deque()
    for ss in se_list:
        queue.append((ss[0],ss[1]))
    # queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not safe(nx, ny):
                continue
            else:
                if farm[nx][ny] == 0:
                    farm[nx][ny] = farm[x][y] + 1
                    queue.append((nx, ny))
                elif farm[nx][ny] > farm[x][y] + 1:
                    farm[nx][ny] = farm[x][y] + 1
                    queue.append((nx, ny))

def solution(farm):
    init_v = 0
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 0:
                return -1
            elif farm[i][j] > init_v:
                init_v = farm[i][j]
    return init_v-1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m = map(int, stdin.readline().rstrip().split())
farm = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]
se_list = start(farm)
# print(se_list)
# for ee in se_list:
#     BFS(ee[0], ee[1])
#     for j in range(4):
#         print(*farm[j])
#     print()
print(solution(farm))