#N행 M열 로테이션 L번
N, M, L = map(int, input().split())

BRD = [list(map(int, input().split())) for _ in range(N)]
newBRD = [[0 for x in range(M)] for y in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 1. rotation만 하는 함수를 만든다.
# 중심부터 테두리까지 가면서 rotation 함수를 돌려준다.
# rotation 함수는 BRD 자체를 바꿔준다.
# 한 rotation이 끝나면 행의 합을 더해준다.
def rotation(r,c):
    newR = r
    newC = c
    pre = BRD[r][c]
    for i in range(4):
        while 1:
            if 0 <= newR+dr[i] < N and 0 <= newC+dc[i] < M and newBRD[newR+dr[i]][newC+dc[i]] == 0:
                temp = BRD[newR+dr[i]][newC+dc[i]]
                BRD[newR+dr[i]][newC+dc[i]] = pre
                pre = temp
                newR += dr[i]
                newC += dc[i]
            else:
                break

                

for l in range(L):
    r, c, s = map(int, input().split())
    for i in range(s):
        print(r-1-i, c-1-i)
        rotation(r-1-i, c-1-i)

for i in range(N):
    print(*BRD[i])
