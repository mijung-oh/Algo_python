N = int(input())

p = [[0 for x in range(101)] for y in range(101)]
for n in range(N):
    stX, stY, height, width = map(int, input().split())


    for i in range(height):
        for j in range(width):
            p[stX+i][stY+j] = 1


    area = 0         
    for i in range(101):
        for j in range(101):
            if p[i][j] == 1:
                area += 1

    print(area)