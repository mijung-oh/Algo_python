def checkAllDragon():
    result = 0
    for i in range(100):
        for j in range(100):
            if BRD[i][j] and BRD[i+1][j] and BRD[i][j+1] and BRD[i+1][j+1]:
                result += 1
    return result

def dragonCurve(D, dragon, G, en_r, en_c):
    if G == 0:
        return
    print(D, dragon)
    new_r = en_r
    new_c = en_c

    for d in D:
        dr = direction[d][0]
        dc = direction[d][1]
        new_r += dr
        new_c += dc
        print("체크될 위치: ", G, new_r, new_c)
        BRD[new_r][new_c] = 1

    new_d = []
    for i in range(len(dragon)-1, -1, -1):
        new_d.append((dragon[i]+3) % 4)
    dragonCurve(new_d, dragon + new_d, G-1, new_r, new_c)


direction = {
    0: (0, 1),
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0)
}

N = int(input())
BRD = [[0 for _ in range(101)] for _ in range(101)]

for n in range(N):
    x, y, d, g = map(int, input().split())
    BRD[x][y] =  1
    # 0세대일 경우
    if g == 0:
        BRD[x+direction[d][0]][y+direction[d][1]] = 1
    else:
        dragonCurve([d, (d+1)%4], [d, (d+3)%4], g, x, y)

for i in range(100):
    print(*BRD[i])
print(checkAllDragon())
