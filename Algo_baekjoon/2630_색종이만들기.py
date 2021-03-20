from collections import deque

N = int(input())
# 1일때 파랑, 0일때 하양

BRD = []
for n in range(N):
    BRD.append(list(map(int, input().split())))
blue_count = 0
white_count = 0

def isColorPaper(x, y, n):
    global blue_count, white_count
    # print(x,y)
    first = BRD[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if 0 <= i <N and 0 <= j < N and BRD[i][j] != first:
                return False

    if first == 1: blue_count += 1
    else: white_count += 1
    return True

q = deque()
q.append((0,0,N))

while q:
    start = q.popleft()
    # print('start', start)
    if not isColorPaper(start[0], start[1], start[2]):
        q.append((start[0], start[1], start[2]//2))
        if 0 <= start[1] + start[2]//2 < N:
            q.append((start[0], start[1] + start[2]//2, start[2]//2))
        if 0 <= start[0] + start[2]//2 < N:
            q.append((start[0] + start[2]//2, start[1], start[2]//2))
        if 0 <= start[0] + start[2]//2 < N and 0 <= start[1] + start[2]//2 < N:
            q.append((start[0] + start[2]//2, start[1] + start[2]//2, start[2]//2))


print(white_count)
print(blue_count)


