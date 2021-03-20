from collections import deque

N = int(input())
# 1일때 파랑, 0일때 하양

BRD = []
for n in range(N):
    BRD.append(list(map(int, input())))

q = deque()
q.append((0,0,N))
result = ''

def Check(x, y, n):
    global result

    first = BRD[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if 0 <= i < N and 0 <= j < N and BRD[i][j] != first:
                return False

    if first == 1: result += '1'
    else: result += '0'
    return True


def isQuad(x, y, n):
    global result
    if Check(x, y, n):
        return
    else:
        result += '('
        isQuad(x, y, n//2)
        isQuad(x, y + n//2, n//2)
        isQuad(x + n//2, y, n//2)
        isQuad(x + n//2, y + n//2, n//2)
        result += ')'

isQuad(0, 0, N)
print(result)

