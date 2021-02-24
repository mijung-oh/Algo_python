T = int(input())



for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input())))
    mid_x = mid_y = len(BRD)//2
    total = 0
    for i in range(len(BRD)//2+1): # i=0,1,2,3
        if i == 0:
            # up
            for j in range(N-mid_y-i): # j=0,1,2,3
                total += BRD[mid_x][mid_y-j]
            # down
            for j in range(1, N-mid_y-i): # j = 1,2,3
                total += BRD[mid_x][mid_y+j]
        else:
            #left
            # up
            for j in range(N - mid_y - i):  # j=0,1,2,3
                total += BRD[mid_x-i][mid_y - j]
            # down
            for j in range(1, N - mid_y - i):  # j = 1,2,3
                total += BRD[mid_x-i][mid_y + j]

            #right
            # up
            for j in range(N - mid_y - i):  # j=0,1,2,3
                total += BRD[mid_x + i][mid_y - j]
            # down
            for j in range(1, N - mid_y - i):  # j = 1,2,3
                total += BRD[mid_x + i][mid_y + j]
    print('#{} {}'.format(tc, total))