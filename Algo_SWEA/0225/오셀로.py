T = int(input())

# 8가지방향
dx = [-1, 0, 1, 1, 1, 0, -1,-1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]


def check(x,y, N, BRD, c):
    # 초기값 저장
    first_x = x
    first_y = y
    loc = [(first_x, first_y)]

    for i in range(8):
        loc2 = []
        while 1:
            # 방향이동한 점이 범위 안에 있으면서 값이 있는 경우
            if 1<= x+dx[i] <= N and 1<=y+dy[i] <= N and BRD[x+dx[i]][y+dy[i]]:
                x += dx[i]
                y += dy[i]
                loc2.append((x,y))
                # 만약 옮겨진 위치가 같은 색깔이면 좌표 리턴
                if BRD[x][y] == c:
                    loc2.pop(-1)
                    loc += loc2
                    break
            else: break
        x = first_x
        y = first_y
    if len(loc) > 1:
        return loc
    # 돌을 놓을 곳이 없는 경우
    return -1



for tc in range(1, T+1):
    # 흑돌: 1 백돌: 2
    N, M = map(int, input().split())
    # 0인덱스 사용 안하기 위해 N+1만큼 생성
    BRD = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # BRD 초기화
    BRD[N // 2][N // 2] = 2
    BRD[N // 2 + 1][N // 2] = 1
    BRD[N // 2][N // 2 + 1] = 1
    BRD[N // 2 + 1][N // 2 + 1] = 2

    # 양쪽 모두 돌을 놓을 것이 없는 경우 게임 끝
    canT = 0
    for m in range(M):
        x, y, c = map(int, input().split())

        #보드에 빈 곳이 없을 경우 break
        ZeroC = 0
        for i in range(len(BRD)):
            for j in range(len(BRD)):
                if BRD[i][j] == 0:
                    ZeroC += 1
        if ZeroC == 2*N+1:
            break

        # 만약 좌표리스트를 받으면
        L = check(x,y,N, BRD, c)
        if L != -1:
            # 받은 리스트를 기준으로 좌표의 색을 바꿔준다.
            for l in L:
                BRD[l[0]][l[1]] = c
        else:
            canT += 1
            if canT == 2:
                break
    # 개수세기
    countB = 0
    countW = 0
    for i in range(1, len(BRD)):
        countB += BRD[i].count(1)
        countW += BRD[i].count(2)
    print('#{} {} {}'.format(tc, countB, countW))



