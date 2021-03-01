T = int(input())
# A는 동서남북 1개씩
# B는 동서남북 2개씩
# C는 동서남북 3개씩
# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def A(x,y,lst):
    for i in range(4):
        newX = x
        newY = y
        if 0<=newX+dx[i] <=len(lst) and 0<=newY+dy[i]<=N:
            newX += dx[i]
            newY += dy[i]
            BRD[newX][newY] = 'X'
    return BRD
def B(x,y,lst):
    for i in range(4):
        newX = x
        newY = y
        for _ in range(2):
            if 0<=newX+dx[i] <=len(lst) and 0<=newY+dy[i]<=N:
                newX += dx[i]
                newY += dy[i]
                BRD[newX][newY] = 'X'
    return BRD
def C(x,y,lst):
    for i in range(4):
        newX = x
        newY = y
        for _ in range(3):
            if 0<=newX+dx[i] <=len(lst) and 0<=newY+dy[i]<=N:
                newX += dx[i]
                newY += dy[i]
                BRD[newX][newY] = 'X'
    return BRD

for tc in range(1, T+1):
    N = int(input())
    BRD = []
    for i in range(N+1):
        BRD.append(list(input()))
    for i in range(len(BRD)):
        for j in range(len(BRD[i])):
            if BRD[i][j] == 'A':
                BRD = A(i, j, BRD)
            if BRD[i][j] == 'B':
                BRD = B(i, j, BRD)
            if BRD[i][j] == C:
                BRD = C(i, j, BRD)
    count = 0
    for i in range(len(BRD)):
        for j in range(len(BRD[i])):
            if BRD[i][j] == 'H':
                count += 1
    print(count)
    for i in range(len(BRD)+1):
        print(*BRD[i])