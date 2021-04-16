import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def f(r, c):
    global cnt, n
        
    for d in [(-1,0), (1,0), (0,-1), (0,1)]:
        R = r + d[0]
        C = c + d[1]
        if 0<=R<n and 0<=C<n and brd[R][C] == brd[r][c] + 1:
            cnt += 1
            f(R, C)
    return cnt


for tc in range(1, T+1):
    n = int(input())
    brd = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = -1
    max_num = 0
    for i in range(len(brd)):
        for j in range(len(brd)):
            cnt = 1
            cnt2 = f(i, j)
            if max_cnt < cnt2:
                max_cnt = cnt2
                max_num = brd[i][j]
            elif max_cnt == cnt2:
                if max_num > brd[i][j]:
                    max_num = brd[i][j]

    print('#{} {} {}'.format(tc, max_num, max_cnt))

