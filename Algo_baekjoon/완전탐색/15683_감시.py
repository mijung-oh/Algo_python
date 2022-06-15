import sys

N, M = map(int, input().split())
# N: 세로, M: 가로
# 상 우 하 좌 = 1 2 3 4
d = {
    1: [(1), (2), (3), (4)],
    2: [(1,3), (2, 4)],
    3: [(1, 2), (2, 3), (3, 4), (4, 1)],
    4: [(1,2,3), (2,3,4), (3,4,1), (4,1,2)],
    5: [(1,2,3,4)]
}
dd = {
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0), 
    4: (0, -1)
}
BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

# 감시영역 표시하기
def check(r, c, direction):
    for d in direction:
        while 1:
            nr = r + dd[d][0]
            nc = c + dd[d][1]
            if 0 <= nr < N and 0 <= nc < M:
                # 벽을 만나면 break
                if BRD[nr][nc] == 6: break
                BRD[nr][nc] = '#'
                r = nr
                c = nc
            else:
                break
                

# 감시영역 표시 지우기
def nonCheck():
    pass

# 사각지대 크기 구하기
def count():
    cnt = 0
    for i in range(len(BRD)):
        for j in range(len(BRD[0])):
            if BRD[i][j] == 0:
                cnt += 1
    return cnt

# CCTV 위치
cctv = []
for i in range(len(BRD)):
        for j in range(len(BRD[0])):
            if 0 < BRD[i][j] < 6:
                cctv.append((i, j))

result = sys.maxsize

def dfs(cctv_idx):
    # 만약 마지막 cctv 일 경우, 사각지대 크기 구하기
    if cctv_idx == len(cctv)-1:
        result = min(result, count())
        return

    # 현재 cctv 위치
    cur_cctv = cctv[cctv_idx]
    # cctv 방향대로 감시영역 표시하기
    for i in d[cur_cctv]:
        check(i)
    # 다음 cctv
    dfs(cctv_idx+1)
    # 감시영역 표시 해제
    for i in d[cur_cctv]:
        nonCheck(i)
