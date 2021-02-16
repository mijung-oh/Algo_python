T = int(input())

for t in range(1, T+1):
    N = int(input())

    snail = [[0 for x in range(N)] for y in range(N)]

    i = 0
    j = -1
    check = 0

    start = 1
    while start != N*N + 1:
        # 오른쪽 방향
        if check == 0:
            j += 1
            if j >= N or snail[i][j]:
                j -= 1
                check += 1
                continue

            snail[i][j] = start
            start += 1

            
        # 아래 방향
        elif check == 1:
            i += 1

            if i >= N or snail[i][j]:
                i -= 1
                check += 1
                continue

            snail[i][j] = start
            start += 1

            
        
        # 왼쪽 방향
        elif check == 2:
            i -= 1
            if i < 0 or snail[i][j]:
                i += 1
                check += 1
                continue

            snail[i][j] = start
            start += 1

        
        # 오른쪽 방향
        elif check == 3:
            j -= 1
            if j < 0 or snail[i][j]:
                j += 1
                check = 0
                continue

            snail[i][j] = start
            start += 1


    print(f'#{t}')   
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()