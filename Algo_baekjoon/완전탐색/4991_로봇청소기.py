from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(brd):
    for r in range(len(brd)):
        for c in range(len(brd[0])):
            if BRD[r][c] == '*':
                return True
    return False

def bfs(brd):
    q = deque()

    # 로봇 청소기 위치
    for r in range(len(brd)):
        for c in range(len(brd[0])):
            if BRD[r][c] == 'o':
                q.append((r,c))
                BRD[r][c] = 0
                break
        if q: break
    
    while q:
        # 만약 현재 더러운 칸이 없을 경우
        if not check(brd):
            break

        r, c = q.popleft()
        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]
            print(nr, len(brd),  nc, len(brd[0]))
            if 0 <= nr < len(brd) and 0 <= nc < len(brd[0]):
                if brd[nr][nc] == '.' or brd[nr][nc] == '*':
                    brd[nr][nc] = brd[r][c] + 1
                    q.append((nr, nc))

C, R = map(int, input().split())
BRD = [list(input()) for _ in range(R)]
bfs(BRD)
for i in range(R):
    print(*BRD[i])