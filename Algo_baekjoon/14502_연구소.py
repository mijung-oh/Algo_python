import copy
from collections import deque


N, M = map(int, input().split())

BRD = []

for n in range(N):
    BRD.append(list(map(int, input().split())))

# 바이러스가 퍼진 뒤 안전지역 카운트
max_safezone = 0
def safezone(brd):
    global N, M, max_safezone
    cnt = 0
    after_brd = copy.deepcopy(brd)
    # print("================ before =================")
    # for i in range(len(after_brd)):
    #     print(*after_brd[i])

    q = deque()
    # 2인 곳을 q에 넣는다.
    for i in range(N):
        for j in range(M):
            if after_brd[i][j] == 2:
                q.append((i,j))
    while q:
        cur_r, cur_c = q.popleft()

        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr = cur_r + d[0]
            nc = cur_c + d[1]
            if 0 <= nr < N and 0 <= nc < M and after_brd[nr][nc] == 0:
                after_brd[nr][nc] = 2
                q.append((nr, nc))

    # print("==============after ===================")
    # for i in range(len(after_brd)):
    #     print(*after_brd[i])
    # 남은 0 개수 세기
    for i in range(N):
        for j in range(M):
            if after_brd[i][j] == 0:
                cnt += 1

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
                brd[i][j] = 1
                cnt += 1
                dfs(brd, cnt)
                brd[i][j] = 0
                cnt -= 1
    


dfs(BRD, 0)
print(max_safezone)
