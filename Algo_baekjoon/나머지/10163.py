N = int(input())

p = [[0 for x in range(101)] for y in range(101)]
for n in range(1, N+1):
    stX, stY, height, width = map(int, input().split())


    for i in range(height):
        for j in range(width):
            p[stX+i][stY+j] = n


for n in range(1, N+1):
    area = 0
    for i in range(101):
        for j in range(101):
            if p[i][j] == n:
                area += 1
    print(area)