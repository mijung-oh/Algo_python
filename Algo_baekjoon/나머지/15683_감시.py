N, M = map(int, input().split())
min_size = N * M

BRD = []
for i in range(N):
    BRD.append(list(map(int, input().split())))

def doCheck(d):
    pass

def notCheck(d):
    pass


cctv_loc = []
for i in range(N):
    for j in range(M):
        if 1 <= BRD[i][j] < 6:
            cctv_loc.append((i,j))

