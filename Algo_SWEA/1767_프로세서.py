T = int(input())

for t in range(T):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))
        
    # 코어의 위치를 배열에 담는다.
    core = []
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N-1 or j == N-1:
                continue
            if BRD[i][j] == 1:
                core.append((i,j))
    # 인덱스로 접근하면서 BRD를 수정하며
    def func(cur_idx, max_core, min_lines):
        # cur_idx가 core 개수 이상이면 끝!
        if cur_idx >= len(core):
            return

        # 해당 좌표로부터 동,서,남,북 중에 뻗을 수 있을 때 다음 좌표로 재귀 돌린다.
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            nextR = core[cur_idx][0] + d[0]
            nextC = core[cur_idx][1] + d[1]
            check = True
            if nextR and nextC:
                check = False

            # 전선 연결되는지 체크
            while not BRD[nextR][nextC]:
                nextR += d[0]
                nextC += d[1]
                if nextR < 0 or nextR >= N or nextC < 0 or nextC >= N:
                    check = False
                    break

            if check:
                # 전선 1로 체크
                cnt = 0
                nextR = core[cur_idx][0] + d[0]
                nextC = core[cur_idx][1] + d[1]
                while 0 <= nextR < N and 0 <= nextC < N:
                    BRD[nextR][nextC] = 1
                    nextR += d[0]
                    nextC += d[1]

                func(cur_idx + 1, max_core + 1, min_lines + cnt)
                # 전선 0으로 체크
                nextR = core[cur_idx][0] + d[0]
                nextC = core[cur_idx][1] + d[1]
                while 0 <= nextR < N and 0 <= nextC < N:
                    BRD[nextR][nextC] = 0
                    nextR += d[0]
                    nextC += d[1]

    # max 코어개수를 구하고, 같을 경우
    # 전선이 작은 경우를 구한다.