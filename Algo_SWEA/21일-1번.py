MAX_SIZE = 100
heapSize = 0


def heapPush(value, heap):
    global heapSize
    if heapSize + 1 > MAX_SIZE:
        return
    heap[heapSize] = value

    current = heapSize
    while current > 0 and heap[current] < heap[(current - 1) // 2]:
        heap[(current - 1) // 2], heap[current] = heap[current], heap[(current - 1) // 2]
        current = (current - 1) // 2

    heapSize = heapSize + 1

T = int(input())


for t in range(T):
    N = int(input())
    BRD = []
    for n in range(N):
        BRD.append(list(map(int, input().split())))

    exitLoc = {}
    isExit = []
    people = []
    visited = {}

    # 탈출구 위치
    for i in range(N):
        for j in range(N):
            if BRD[i][j] == 2:
                exitLoc[(i,j)] = []
    # 탈출구와 사람 사이 거리 넣기
    for i in range(N):
        for j in range(N):
            if BRD[i][j] == 1:
                for k in exitLoc:
                    dist = abs(k[0] - i) + abs(k[1] - j)
                    exitLoc[k].append((dist, i, j))
    while 1:


