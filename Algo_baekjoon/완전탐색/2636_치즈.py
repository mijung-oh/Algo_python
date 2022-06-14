from collections import deque

R, C = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(R)]
time = 0
# 다 녹기 한시간 전 치즈 개수
pre = 0

# 0과 붙어있는 1이 곧 가장자리가 되므로 가장자리를 찾기 위해 0인 부분만 q에 담는 방식으로 돈다
# 0과 붙어있는 1은 q에 넣지 말고 visited만 1로 체크한 뒤 실제 값은 0으로 바꿔준다 => 다음 턴에 q에 담겨지기 위해
while 1:
    visited = [[0 for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    # 1의 개수
    cnt = 0
    while q:
        cur = q.popleft()
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr = cur[0] + d[0]
            nc = cur[1] + d[1]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                # visited 체크
                visited[nr][nc] = 1
                # 다음 칸이 0이면 q에 넣는다.
                if BRD[nr][nc] == 0:
                    q.append((nr, nc))
                else:
                    BRD[nr][nc] = 0
                    # 치즈 개수
                    cnt += 1

    # 만약 BRD에서 1이 찾아지지 않으면 break
    if cnt == 0:
        break
    else:
        time += 1
        pre = cnt
print(time)
print(pre)
                