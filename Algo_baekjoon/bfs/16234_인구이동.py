from collections import deque

N, L, R = map(int, input().split())
BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))
result = 0
def check():
    global L, R, result, N
    returnV = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # BRD를 돌면서 L이상 R이하인지 체크한다.
    for i in range(len(BRD)):
        for j in range(len(BRD)):
            if not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                total = BRD[i][j]
                cnt = 1
                change_list = [(i, j)]
                
                while q:
                    r, c = q.popleft()
                    # 4 방향 노드의 차를 구한다.
                    for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                        nr = d[0] + r
                        nc = d[1] + c
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <=abs(BRD[r][c] - BRD[nr][nc]) <= R:
                            # 인접한 연합국가 찾기
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                            change_list.append((nr, nc))
                            total += BRD[nr][nc]
                            cnt += 1
                # 인구수 변경
                changed_num = total // cnt
                for r, c in change_list:
                    BRD[r][c] = changed_num
                # 인구이동 여부
                if cnt >= 2: 
                    returnV = True
    if returnV:
        result += 1
    return returnV            

while 1:
    r = check()
    if not r: break
print(result)
