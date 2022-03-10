import copy


N, M = map(int, input().split())

BRD = []

for n in range(N):
    BRD.append(list(map(int, input().split())))

# 바이러스가 퍼진 뒤 안전지역 카운트
max_safezone = 0
def safezone(brd):
    global N, M, max_safezone
    cnt = 0
    afterBrd = copy.deepcopy(brd)
    
    # print("===============================")
    # for i in range(len(brd)):
    #     print(*brd[i])

    for i in range(N):
        for j in range(M):
            if afterBrd[i][j] == 2 :
                # 상하좌우로 0인 부분들은 다 1로 설정
                for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr = i + d[0]
                    nc = j + d[1]
                    while 0 <= nr < N and 0 <= nc < M and afterBrd[nr][nc] == 0:
                        afterBrd[nr][nc] = 1
                        nr += d[0]
                        nc += d[1]
    # 남은 0 개수 세기
    for i in range(N):
        for j in range(M):
            if afterBrd[i][j] == 0:
                cnt += 1
    
    if cnt == 31:
        print("===================================")
        for i in range(len(brd)):
            print(*afterBrd[i])

    if max_safezone < cnt:
        max_safezone = cnt
    return

def dfs(brd, cnt):
    global max_safezone, N, M
    # 만약 설치한 벽이 3개이면 safezone 실행 후 최대 안전지역 크기 구하기
    if cnt == 3:
        safezone(brd)
        return

    for i in range(N):
        for j in range(M):
            if brd[i][j] == 0:
                if i == 3 and j == 5:
                    print(cnt, "hihi")
                # print("cnt : " , cnt , " i, j : ", i, j)
                brd[i][j] = 1
                cnt += 1
                dfs(brd, cnt)
                brd[i][j] = 0
                cnt -= 1
    


dfs(BRD, 0)
print("result : " , max_safezone)
