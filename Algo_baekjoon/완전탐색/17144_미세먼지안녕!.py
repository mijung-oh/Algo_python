R, C, T = map(int, input().split())
PRE_BRD = [list(map(int, input().split())) for _ in range(R)]
POST_BRD = PRE_BRD[::]
# 공기청정기 위치
u, d = 0, 0
for r in range(R):
    for c in range(C):
        if PRE_BRD[r][c] == -1:
            u = [r,c]
            d = [r+1, c]
            break
    if u: break

# T초동안
while T:
    T -= 1
    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if PRE_BRD[r][c] >= 0:
                # 확산시키기
                # 확산된 방향 개수
                cnt = 0
                for d in [(1,0), (0,1), (0,-1), (-1,0)]:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < R and 0 <= nc < C and PRE_BRD[nr][nc] != -1:
                        # POST_BRD를 업데이트 시킨다.
                        POST_BRD[nr][nc] += PRE_BRD[r][c] // 5
                        cnt += 1
                POST_BRD[r][c] -= (PRE_BRD[r][c] // 5) * cnt
    PRE_BRD = POST_BRD[::]

    # 공기청정기 작동
    # 만약 r gap이 1이면
    if u-d == [1,0]:
        # 만약 u와 d가 열을 벗어나게 된다면
        if u[1] + 1 >= C:
            # 위아래로 간다.
            u += [1,0]
            d -= [1,0]
        else:
            # 오른쪽으로 간다.
            u += [0,1]
            d += [0,1]
    elif u-d == [R-1,0]:
        # 왼쪽 끝일 경우 아래 위로 이동
        if u[1] == 0:
            u -= [1,0]
            d += [1,0]
        else:
            # 오른쪽 끝일 경우 위 아래로 이동
            u += [1,0]
            d -= [1,0]
    

