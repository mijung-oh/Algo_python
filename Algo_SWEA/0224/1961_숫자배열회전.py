T = int(input())


def rotation(lst):
    lst2 = []
    for c in range(len(lst)):
        R = []
        for r in range(len(lst)-1, -1, -1):
            R.append(lst[r][c])
        lst2.append(R)
    return lst2


for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))
    ro_90 = rotation(BRD)
    ro_180 = rotation(ro_90)
    ro_270 = rotation(ro_180)

    print('#{}'.format(tc))
    for i in range(len(BRD)):
        for j in range(len(BRD)):
            print(ro_90[i][j], end='')
        print(' ', end='')
        for j in range(len(BRD)):
            print(ro_180[i][j], end='')
        print(' ', end='')
        for j in range(len(BRD)):
            print(ro_270[i][j], end='')
        print()
