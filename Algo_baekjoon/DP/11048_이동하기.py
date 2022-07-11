N, M = map(int, input().split())
BRD = [list(map(int, input().split())) for _ in range(N)]
NEWBRD = [[0 for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        up = NEWBRD[r-1][c] if r-1 >= 0 else 0
        left = NEWBRD[r][c-1] if c-1 >= 0 else 0
        cross = NEWBRD[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0

        NEWBRD[r][c] = max(up, max(left, cross)) + BRD[r][c]
# print()
# for i in range(N):
#     print(*NEWBRD[i])
print(NEWBRD[N-1][M-1])