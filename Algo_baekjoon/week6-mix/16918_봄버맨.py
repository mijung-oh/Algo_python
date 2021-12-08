R, C, N = map(int, input().split())
BRD = []
for r in range(R):
    BRD.append(list(input()))

# 폭탄 놓는 함수
def letBomb():
    for i in range(len(BRD)):
        for j in range(len(BRD[0])):
            if BRD[i][j] == '.':
                BRD[i][j] = 'O'

# 폭탄 터트리는 함수
def explosion(lst):
    while lst:
        curR, curC = lst.pop()
        BRD[curR][curC] = '.'
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            newR = curR + d[0]
            newC = curC + d[1]
            if 0 <= newR < len(BRD) and 0 <= newC < len(BRD[0]):
                BRD[newR][newC] = '.'

check = True
letBomb_loc = []
bomb_loc = []
for n in range(1, N): # N=5 => 0 1 2 3 4 => 1 2 3 4
    if check:
        # 원래 폭탄이 있던 자리를 저장해놓는다.
        for i in range(len(BRD)):
            for j in range(len(BRD[0])):
                if BRD[i][j] == 'O':
                    bomb_loc.append((i,j))
        letBomb()
    else:
        explosion(bomb_loc)
    check = not check

for i in range(len(BRD)):
    for j in range(len(BRD[0])):
        print(BRD[i][j], end="")
    print()