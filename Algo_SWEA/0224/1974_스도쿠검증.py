T = int(input())

for tc in range(1, T+1):
    sdoku = []
    check = 1
    sub_sdoku = []
    for i in range(9):
        sdoku.append(list(map(int, input().split())))
    # 3x3 서브배열 담아놓기
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(i,j)
            sub = []
            for x in range(3):
                for y in range(3):
                    sub.append(sdoku[i+x][j+y])
            sub_sdoku.append(sub)

    # 스도쿠 검증
    for i in range(9):
        for j in range(9):
            target = sdoku[i][j]
            # 가로
            if sdoku[i].count(target) == 2:
                check = 0
                break
            # 세로
            col = []
            for k in range(9):
                col.append(sdoku[k][j])
            if col.count(target) == 2:
                check = 0
                break
            # 네모박스
            for k in range(9):
                if sub_sdoku[k].count(target) == 2:
                    check = 0
                    break
    print('#{} {}'.format(tc, check))

