N = int(input())

count = 0
# 인덱스가 0일땐 가로, 1일땐 세로, 2일땐 대각선
state_move = [[(0,1), (1,1)], [(1,0), (1,1)], [(0,1), (1,0), (1,1)]]
# visited = [[0 for _ in range(N)] for _ in range(N)]
BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

#초기화
# visited[0][0] = 1
# visited[0][1] = 1
# 갈 수 있는 칸이 범위 안에 있는지 + 0이 맞는지 확인!

# 대각선일경우 나머지 2칸이 범위 안에 있는지 + 0이 맞는지 확인
# def crossCheck(x,y):
#     if x-1 < 0 or y-1 < 0:
#         return False
#     if BRD[x-1][y] or BRD[x][y-1]:
#         return False
#     return True

def dfs(x, y, state):
    global count

    if x == N-1 and y == N-1:
        count += 1
        return

    for i in state_move[state]: # (0,1), (1,1)
        newX = x + i[0]
        newY = y + i[1]
        if 0<= newX < N and 0<= newY < N and BRD[newX][newY] == 0:
            # 가로일경우
            if i == (0,1):
                # visited[newX][newY] = 1
                dfs(newX, newY, 0)
                # visited[newX][newY] = 0
            elif i == (1,0):
                # visited[newX][newY] = 1
                dfs(newX, newY, 1)
                # visited[newX][newY] = 0
            # 대각선이면 3칸이 0이어야함
            elif i == (1,1) and 0<= newX-1 < N and 0 <= newY-1 < N and BRD[newX-1][newY]==0 and BRD[newX][newY-1] == 0:
                # visited[newX][newY] = 1
                dfs(newX, newY, 2)
                # visited[newX][newY] = 0


        
if BRD[N-1][N-1]:
    print(0)
else: 
    dfs(0,1,0)
    print(count)         
