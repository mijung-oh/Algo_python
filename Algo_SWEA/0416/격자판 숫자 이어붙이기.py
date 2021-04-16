T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0,0]

def f(r, c, result):
    if len(result) == 7:
        make.add(result)
        return
    
    for i in range(4):
        newR = r + dr[i]
        newC = c + dc[i]
        if 0 <= newR < 4 and 0 <= newC < 4 and len(result) + 1 <= 7:
            f(newR, newC, result + str(BRD[newR][newC]))


for tc in range(1, T+1):
    BRD = []
    for i in range(4):
        BRD.append(list(map(int, input().split())))
    
    make = set()
    for i in range(4):
        for j in range(4):
            f(i, j, str(BRD[i][j]))
    print('#{} {}'.format(tc, len(make)))