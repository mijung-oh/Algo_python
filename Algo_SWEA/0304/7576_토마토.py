from collections import deque

def bfs():
    visited = [[0 for x in range(N)] for y in range(M)]
    q = deque()
    # BRD에서 1인 부분을 먼저 추가하기.
    # -1인 것의 개수 세기
    Mcount = 0
    for i in range(M):
        for j in range(N):
            if BRD[i][j] == 1:
                q.append((i,j))
            elif BRD[i][j] == -1:
                Mcount += 1
    count = len(q)
    while q:
        new = q.popleft()
        for i in range(4):
            newX = new[0]+dx[i]
            newY = new[1]+dy[i]
            if 0<=newX<M and 0<=newY<N and visited[newX][newY] == 0 and BRD[newX][newY] == 0:
                visited[newX][newY] = visited[new[0]][new[1]] + 1
                q.append((newX, newY))
                # 익을 토마토의 개수?
                count += 1
            # 모든 토마토가 익은 경우
            if count == N*M - Mcount:
                print(newX, newY)
                # 이게 왜 0???
                print(visited[-1][0])
                return visited[newX][newY]

    return -1

# N은 열 M은 행 개수
N, M = map(int, input().split())
# x는 행 y는 열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

BRD = []
for m in range(M):
    BRD.append(list(map(int, input().split())))
print(bfs())

