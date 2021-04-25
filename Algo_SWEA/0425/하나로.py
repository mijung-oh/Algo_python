import heapq

T = int(input())

def dijk():
    global r
    heap = []
    total = 0
    heapq.heappush(heap, (0, 0))
    while heap:
        cost, idx = heapq.heappop(heap)
        visited[idx] = 1
        for i in range(len(D)):
            if visited[i] == 0:
                if D[i] > ((x[i]-x[idx]) ** 2 + (y[i] - y[idx]) ** 2) * r:
                    D[i] = ((x[i]-x[idx]) ** 2 + (y[i] - y[idx]) ** 2) * r
                    heapq.heappush(heap, (D[i], i))
    return round(sum(D))



for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    r = float(input())
    D = [9e+20]*N
    visited = [0] * N
    D[0] = 0
    # 세율 * 거리 ** 2 만큼 D 초기화
    # for i in range(1, N):
    #     D.append(((x[i]-x[0]) ** 2 + (y[i] - y[0]) ** 2) * r)
    # visited[0] = 1
    print('#{} {}'.format(tc, dijk()))