T = int(input())

# core_cnt = 몇개의 코어가 연결돼있는지?
# 현재 코어 배열에 5개의 코어가 있고
# current는 cores 배열에 접근할 index 0~4
def bruteForce(current, core_cnt, total):
    global N, min_total, max_core
    # 만약 current가 len(cores)-1과 같아진 경우
    # 모든 코어를 다 돌게 됨
    if current == len(cores):
        # 모든 코어가 성공적이었을 경우
        if core_cnt == len(cores):
            max_core = core_cnt
            # total를 비교한다.
            if total < min_total:
                min_total = total
        elif core_cnt < len(cores):
            # 코어개수를 비교한다.
            if core_cnt > max_core:
                max_core = core_cnt
        return

    cr = cores[current][0]
    cc = cores[current][1]
    is_possible = 0
    # 방향은 동서남북
    for d in [(0,1), (0,-1), (1,0), (-1,0)]:
        t = 0
        nr = cr
        nc = cc
        check = 0
        # 다음 노드의 BRD 값이 1인 경우 back
        # 다음 노드가 이미 visited인 경우 back
        while 0<nr<N-1 and 0<nc<N-1:
            nr += d[0]
            nc += d[1]
            t += 1

            if visited[nr][nc] or BRD[nr][nc]:
                # print(nr, nc, d)
                check = 1
                # visited를 다시 0으로 바꿔준다.
                while t>0:
                    nr -= d[0]
                    nc -= d[1]
                    t -= 1
                    if t:
                        visited[nr][nc] = 0
                break
            if check: break
            visited[nr][nc] = 1

        if check: continue
        # for v in range(N):
        #     print(*visited[v])
        # print()
        
        is_possible = 1
        bruteForce(current+1, core_cnt+1, total+t)
        while t>0:
            visited[nr][nc] = 0
            nr -= d[0]
            nc -= d[1]
            t -= 1

    # 4방향 다 실패한 경우
    if not is_possible:
        bruteForce(current+1, core_cnt, total)

            
            


for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for n in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cores = []
    max_core = -1
    min_total = 0xffffffff
    for i in range(1, len(BRD)-1):
        for j in range(1, len(BRD)-1):
            if BRD[i][j]:
                visited[i][j]=1
                cores.append((i,j))
    bruteForce(0, 0, 0)
    print('#{} {}'.format(tc, min_total))