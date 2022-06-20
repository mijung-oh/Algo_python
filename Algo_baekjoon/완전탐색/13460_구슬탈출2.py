from collections import deque
import sys

R, C = map(int, input().split())
BRD = [list(input()) for _ in range(R)]


# 1. 현재 구슬 위치를 q에 저장한다.
rr = rc = br = bc = 0
for r in range(R):
    for c in range(C):
        if BRD[r][c] == 'B':
            br, bc = r, c
        elif BRD[r][c] == 'R':
            rr, rc = r, c
    if rr and rc and br and bc: break

count = 0
def bfs():
    global count
    q = deque()
    q.append((rr, rc, br, bc))

    # 구슬이 계속 움직이도록 while True를 돌린다.

    # 방문 여부
    visited = [(rr, rc, br, bc)]

    while q:
        
        if count > 10:
            return False

        for _ in range(len(q)):
            cur_rr, cur_rc, cur_br, cur_bc = q.popleft()

            if BRD[cur_rr][cur_rc] == 'O':
                return True
            # 2. 네 방향으로 움직인다.
            for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                cur_rr2, cur_rc2, cur_br2, cur_bc2 = cur_rr, cur_rc, cur_br, cur_bc

                r_cnt, b_cnt = 0, 0
                # 2-1 RED 구슬 움직이기
                while True:
                    # 구슬 위치 업데이트
                    nrr, nrc = cur_rr2 + d[0], cur_rc2 + d[1]
                    r_cnt += 1
                    if 0 <= nrr < R and 0 <= nrc < C:
                        # 다음 위치가 벽일 경우,
                        if BRD[nrr][nrc] == '#':
                            break
                        cur_rr2, cur_rc2 = nrr, nrc
                        # 다음 위치가 구멍일 경우
                        if BRD[nrr][nrc] == 'O':
                            break
                
                # 2-1 Blue 구슬 움직이기
                while True:
                    # 구슬 위치 업데이트
                    nbr, nbc = cur_br2 + d[0], cur_bc2 + d[1]
                    b_cnt += 1
                    if 0 <= nbr < R and 0 <= nbc < C:
                        # 다음 위치가 벽일 경우,
                        if BRD[nbr][nbc] == '#':
                            break
                        cur_br2, cur_bc2 = nbr, nbc
                        if BRD[nbr][nbc] == 'O':
                            break

                # 파란 공이 구멍에 들어간 경우
                if BRD[cur_br2][cur_bc2] == 'O':
                    continue

                # 빨간 공이 구멍에 들어간 경우
                # if BRD[cur_rr2][cur_rc2] == 'O':
                #     check = True
                #     break
                
                # 파란 공과 빨간 공이 겹칠 경우
                if cur_br2 == cur_rr2 and cur_bc2 == cur_rc2:
                    # 더 많이 이동한 공이 한 칸 뒤로 간다.
                    if r_cnt > b_cnt:
                        cur_rr2 -= d[0]
                        cur_rc2 -= d[1]
                    else:
                        cur_br2 -= d[0]
                        cur_bc2 -= d[1]
                
                if ((cur_rr2, cur_rc2, cur_br2, cur_bc2)) in visited:
                    continue
        
          

                q.append((cur_rr2, cur_rc2, cur_br2, cur_bc2))
                visited.append((cur_rr2, cur_rc2, cur_br2, cur_bc2))

        count += 1
    return False 

if bfs():
    print(count)
else:
    print(-1)
