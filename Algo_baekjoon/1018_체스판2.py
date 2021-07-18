from collections import deque

        
# 몇개 고쳐야하는지 세기
def bruteforce(visited, r, c):
    global N, M
    brd = BRD[:]
    cnt = 0
    dq = deque()
    dq.append((r,c))
    while dq:
        curR, curC = dq.popleft()
        # 오른쪽, 아래가 다른 경우 변경 후 dq에 삽입
        for d in [(0,1), (1,0)]:
            nextR = curR + d[0]
            nextC = curC + d[1]
            if r <= nextR < r+8 and c <= nextC < c+8 and brd[curR][curC] == brd[nextR][nextC]:
                brd[nextR][nextC] = 'B' if brd[curR][curC] == 'W' else 'W'
                cnt += 1
                print("?")
            if r <= nextR < r+8 and c <= nextC < c+8 and not visited[nextR][nextC]:
                dq.append((nextR,nextC))
                visited[nextR][nextC] = 1
    
    for i in range(8):
        print(*brd[i])
    return cnt
    
    
N, M = map(int, input().split())
BRD = []
for n in range(N):
    BRD.append(list(input()))

min_cnt = 0xffff
# 8*8로 나누기
for r in range(len(BRD)-8+1): # i: 0 1 2
    for c in range(len(BRD)-8+1):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        result = bruteforce(visited, r, c)
        if result < min_cnt:
            min_cnt = result
    
print(min_cnt)
    
