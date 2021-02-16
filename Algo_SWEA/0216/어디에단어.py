T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = []
    for n in range(N):
        puzzle.append(list(map(int, input().split())))

    count = 0
    for i in range(N):
        check_r = 0
        check_c = 0
        for j in range(N):
            # 가로에 있는지 확인
            if puzzle[i][j] == 1:
                check_r += 1
            else:
                if check_r == K:
                    count += 1

                check_r = 0
            # 세로에 있는지 확인
            if puzzle[j][i] == 1:
                check_c += 1
            else:
                if check_c == K:
                    count += 1
                check_c = 0
        
        if check_r == K:
            count += 1

        if check_c == K:
            count += 1
    
   

    print(f'#{t} {count}')
