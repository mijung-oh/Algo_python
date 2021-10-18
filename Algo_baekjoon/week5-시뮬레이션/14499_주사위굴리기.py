N, M, r, c, K = map(int, input().split())


BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

ju = [0,0,0,0,0,0]

order = list(map(int, input().split()))
for o in order:
    # 동
    if o == 1:
        c += 1
        if c < 0 or c >= M:
            c -= 1
            continue
        # 주사위 change
        ju[0], ju[3] = ju[3], ju[0]
        ju[2], ju[3] = ju[3], ju[2] 

        if BRD[r][c] == 0:
            # 주사위 바닥에 있는 수가 칸에 복사된다.
            BRD[r][c] = ju[5]
        else:
            ju[5] = BRD[r][c]
            BRD[r][c] = 0

    # 서
    elif o == 2:
        c -= 1
        if c < 0 or c >= M:
            c += 1
            continue
        # 주사위 change
        ju[2], ju[3] = ju[3], ju[2]
        ju[0], ju[3] = ju[3], ju[0]

        if BRD[r][c] == 0:
            # 주사위 바닥에 있는 수가 칸에 복사된다.
            BRD[r][c] = ju[5]
        else:
            ju[5] = BRD[r][c]
            BRD[r][c] = 0

    # 북
    elif o ==3:
        r -= 1
        if r < 0 or r >= N:
            r += 1
            continue

        # 주사위 change
        ju[0], ju[1] = ju[1], ju[0]
        ju[1], ju[4] = ju[4], ju[1]
        ju[1], ju[5] = ju[5], ju[1]

        if BRD[r][c] == 0:
            # 주사위 바닥에 있는 수가 칸에 복사된다.
            BRD[r][c] = ju[5]
        else:
            ju[5] = BRD[r][c]
            BRD[r][c] = 0

    # 남
    elif o == 4:
        r += 1
        if r < 0 or r >= N:
            r -= 1
            continue
        # 주사위 change
        ju[0], ju[1] = ju[1], ju[0]
        ju[1], ju[5] = ju[5], ju[1]
        ju[4], ju[5] = ju[5], ju[4]

        if BRD[r][c] == 0:
            # 주사위 바닥에 있는 수가 칸에 복사된다.
            BRD[r][c] = ju[5]
        else:
            ju[5] = BRD[r][c]
            BRD[r][c] = 0
    print(ju[0])