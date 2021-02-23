# 북, 남일 경우 왼쪽에서 가로방향으로 +
# 북일경우 y좌표는 0, 남일경우 y좌표는 c
# 서, 남쪽 방향일경우 세로방향으로 +
# 서일경우 x좌표는 0, 동일경우 x좌표는 r
# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
loc = []
r, c = map(int, input().split())
N = int(input())

def search(start, end):
    if 
    for i in range(4):
        if start[0]+dx[i] > r or start[1]+dy[i] > c or start[0]+dx[i] < 0 or start[1]+dy[i] < 0:
            continue
        new_st = (start[0]+dx[i], start[1]+dy[i])
        search(new_st, end)


for n in range(N+1):
    D, L = map(int, input().split())
    # 북쪽
    if D == 1:
        loc.append((L, 0))
    # 남
    elif D == 2:
        loc.append((L, c))
    # 서
    elif D == 3:
        loc.append((0, L))
    # 동
    else:
        loc.append((L, r))

# 동근이 위치
D_L = loc[-1]
# 총 거리
total = 0
for i in range(len(loc)-1):
    # #  같은 줄에 있는 경우
    # if D_L[0] == loc[i][0]:
    #     total += abs(loc[i][1]-D_L[1])
    # elif D_L[1] == loc[i][1]:
    #     total += abs(loc[i][0]-D_L[0])
    # # 다른 줄에 있는 경우
    # else:
    search(D_L, Goal)