# 좌우상하
dx = [0,0,-1,1]
dy = [-1,1,0,0]
loc = []
# c: 가로길이(열수) r 세로길이(행수)
c, r = map(int, input().split())
N = int(input())

def search(start, end):
    max_len = -1
    # start점 기준으로 양쪽 혹은 위아래 두 개의 점만 들어간다.
    visited = []
    # 직전 x,y
    pre_x = 0
    pre_y = 0
    check = 0
    for _ in range(2):
        count = 0
        # 초기값
        x = start[0]
        y = start[1]
        while 1:
            for i in range(4): # 좌 우 상 하
                if check:
                    break
                while 1:
                    # 아예 범위를 벗어나거나 전꺼랑 같은 경우
                    if x+dx[i] < 0 or x+dx[i] > r or y+dy[i] < 0 or y+dy[i] > c or (pre_x,pre_y) == (x+dx[i], y+dy[i]):
                        break
                    # 테두리인 경우
                    if (x==0 and 0<=y<=c) or (y==0 and 0<=x<=r) or (x==r and 0<=y<=c) or (y==c and 0<=y<=c):
                        count += 1
                        pre_x = x
                        pre_y = y
                        x += dx[i]
                        y += dy[i]
                        # visit했던 원소면 안됨
                        if len(visited) and (x,y) == visited[0]:
                            break
                        if count == 1:
                            visited.append((x,y))
                        # 도착하면 max랑 비교해서 큰거 넣어주기
                        if (x,y) == end:
                            check = 1
                            if max_len < count:
                                max_len = count
                                break
                    else: break
        # while 끝내기
        if check:
            check = 0
            break
    return max_len








for n in range(N+1):
    D, L = map(int, input().split())
    # 북쪽
    if D == 1:
        loc.append((0, L))
    # 남
    elif D == 2:
        loc.append((r, L))
    # 서
    elif D == 3:
        loc.append((L, 0))
    # 동
    else:
        loc.append((L, c))

# 동근이 위치
D_L = loc[-1]
# 총 거리
total = 0

print(search(D_L, (0,4)))