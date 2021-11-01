BRD = [[0 for x in range(101)] for y in range(101)]
for _ in range(4):
    x,y,x2,y2 = map(int, input().split())
    for i in range(x, x2):
        for j in range(y, y2):
            BRD[i][j] = 1

count = 0
for i in range(101):
    for j in range(101):
        if BRD[i][j] == 1:
            count += 1
print(count)