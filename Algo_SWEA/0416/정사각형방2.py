import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


for tc in range(1, T+1):
    n = int(input())
    BRD = [list(map(int, input().split())) for _ in range(n)]
    # print(BRD)
    v= [0] * (n**2 + 1)
    for i in range(n):
        for j in range(n):
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0<= i+d[0] <n and 0<= j+d[1] <n and BRD[i+d[0]][j+d[1]] == BRD[i][j] + 1:
                    v[BRD[i][j]] = 1
                    break
    max_cnt = -1
    min_num = 0
    cnt = 0
    for idx, vv in enumerate(v):
        if vv == 1:
           cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                min_num = idx - cnt
            cnt = 0



    print('#{} {} {}'.format(tc, min_num, max_cnt+1))

