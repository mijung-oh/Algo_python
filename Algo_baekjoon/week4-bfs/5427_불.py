'''
1. 동서남북이 모두 벽인 경우는 바로 false
2. 불 -> 상근 순으로 bfs 돌리기.
'''
from collections import deque

def bfs(brd, W, H):
    # 상근이 위치와 불 위치 저장하기
    fire = deque()
    sanggeun = deque()
    move = 2000
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == '@':
                sanggeun.append((i,j))
                brd[i][j] = 1
            elif brd[i][j] == '*':
                fire.append((i,j))
    
    while sanggeun:
        # 불
        fire_len = len(fire)
        for i in range(fire_len):
            cur_fire = fire.popleft()
            for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                next_fire_r = cur_fire[0] + d[0]
                next_fire_c = cur_fire[1] + d[1]
            
                if 0 <= next_fire_r < H and 0 <= next_fire_c < W and brd[next_fire_r][next_fire_c] != "#" and brd[next_fire_r][next_fire_c] != "*":
                    fire.append((next_fire_r, next_fire_c))
                    if brd[next_fire_r][next_fire_c] == '.':
                        brd[next_fire_r][next_fire_c] = "*"

        # 상근이
        sanggeun_len = len(sanggeun)
        for i in range(sanggeun_len):
            cur_sanggeun = sanggeun.popleft()
            
            for d in [(1,0), (0,1), (-1,0), (0,-1)]:
                next_sanggeun_r = cur_sanggeun[0] + d[0]
                next_sanggeun_c = cur_sanggeun[1] + d[1]
                
                if 0 <= next_sanggeun_r < H and 0 <= next_sanggeun_c < W and brd[next_sanggeun_r][next_sanggeun_c] == ".":
                    sanggeun.append((next_sanggeun_r, next_sanggeun_c))
                    brd[next_sanggeun_r][next_sanggeun_c] = brd[cur_sanggeun[0]][cur_sanggeun[1]] + 1 
                elif next_sanggeun_r < 0 or next_sanggeun_r >= H or next_sanggeun_c < 0 or next_sanggeun_c >= W:
                    return brd[cur_sanggeun[0]][cur_sanggeun[1]]
                    
        # for i in range(len(brd)):
        #     print(*brd[i])
        # print()
    return move



T = int(input())
for t in range(T):
    W, H = map(int, input().split())
    BRD = []
    for h in range(H):
        BRD.append(list(input()))

    for i in range(len(BRD)):
        print(*BRD[i])
    print()

    result = bfs(BRD, W, H)
    if result == 2000:
        print("IMPOSSIBLE")
    else:
        print(result)