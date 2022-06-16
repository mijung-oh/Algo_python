from collections import deque

# N, M = 세로, 가로
R, C = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(R)]
time = 0

# 그냥 가장자리이면 q에 담는 형식으로 가장자리를 찾으면 된다.
# 두 변이 공기와 접촉하되 치즈 내부공기와 외부공기가 구분되어야 한다.

# => 외부공기 체크하는데 1로 가로막혔던 부분이 2로 바껴서 결국 뚫리는걸 고려하지 못한다.
# 외부공기 체크 자체를 bfs로 체크할 것.
# 외부공기 체크
def outAirCheck():
    # 왼쪽 방향
    for r in range(R):
        for c in range(C):
            if BRD[r][c] == 0:
                BRD[r][c] = 2
            elif BRD[r][c] == 1:
                break
    # 오른쪽 방향
    for r in range(R):
        for c in range(C-1, -1, -1):
            if BRD[r][c] == 0:
                BRD[r][c] = 2
            elif BRD[r][c] == 1:
                break
    # up-down 방향
    for c in range(C):
        for r in range(R):
            if BRD[r][c] == 0:
                BRD[r][c] = 2
            elif BRD[r][c] == 1:
                break
    # down-up 방향
    for c in range(C):
        for r in range(R-1, -1, -1):
            if BRD[r][c] == 0:
                BRD[r][c] = 2
            elif BRD[r][c] == 1:
                break

while 1:
    # 외부공기 체크한다.
    outAirCheck()
    # 마주한 변 2개 이상이 외부공기인지 카운트한다.
    q = deque()
    for r in range(R):
        for c in range(C):
            if BRD[r][c] == 1:
                cnt = 0
                # 위
                if r-1 >= 0 and BRD[r-1][c] == 2:
                    cnt += 1
                # 아래
                if r+1 < R and BRD[r+1][c] == 2:
                    cnt += 1
                # 왼
                if c-1 >= 0 and BRD[r][c-1] == 2:
                    cnt += 1
                #오른
                if c+1 < C and BRD[r][c+1] == 2:
                    cnt += 1
                if cnt >= 2:
                    # 곧 녹을 치즈
                    q.append([r,c])
    # 곧 녹을 치즈가 있는 상태라면 time+1 해주고 상태를 2로 변경한다.
    if q:
        time += 1
        while q:
            cheese = q.popleft()
            BRD[cheese[0]][cheese[1]] = 2
    else:
        break
    print("그래프")
    for i in range(len(BRD)):
        print(*BRD[i])
print(time)