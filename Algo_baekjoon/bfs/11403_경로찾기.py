import sys
input = sys.stdin.readline

N = int(input())

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))

for k in range(0, N) :
    for i in range(0, N) :
        for j in range(0, N):
            if BRD[i][k] and BRD[k][j] :
                BRD[i][j] = 1
for i in range(len(BRD)):
    print(*BRD[i])