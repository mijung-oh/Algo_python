BRD = []
for i in range(10):
    BRD.append(list(map(int, input().split())))

for i in range(10):
    for j in range(10):
        if BRD[i][j] == 1:
            