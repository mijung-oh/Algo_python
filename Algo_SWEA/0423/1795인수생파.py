import sys, heapq
sys.stdin = open('input.txt', 'r')

# X는 시작점
def dijk(D, X, graph):
    global N
    U = [X]
    current = X
    while len(U) != N:
        # D 업데이트
        for i in range(1, len(D)):
            if i in U or graph[current][i] == 0: continue
            if D[i] > D[current]+graph[current][i]:
                D[i] = D[current]+graph[current][i]

        min_cost = 0xffff
        min_node = 0

        for idx, d in enumerate(D):
            # graph에는 (가중치, next node)
            # 가려는 곳이 visited에 없으면서 최솟값이어야 한다.
            if idx in U: continue

            if min_cost > d:
                min_cost = d
                min_node = idx

        U.append(min_node)
        current = min_node

        current = next_node
        
    return



T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph1 = [[0xffff for _ in range(N+1)] for _ in range(N+1)]
    graph2 = [[0xffff for _ in range(N+1)] for _ in range(N+1)]

    # 시작점과 도착점을 반대로 받기
    for m in range(M):
        st, en, cost = map(int, input().split())
        graph1[st][en] = cost
        graph2[en][st] = cost

    # X번에서 각각의 점들까지 얼마나 걸리는지 저장하는 배열 
    # == 각각 점들에서 X까지의 거리
    D1 = [0xffff] * (N+1)
    D1[X] = 0
    dijk(D1, X, graph1)

    # X번에서 각각 점들까지 거리
    D2 = [0xffff] * (N+1)
    D2[X] = 0
    dijk(D2, X, graph2)

    maxV = -1
    for d in range(1, N+1):
        # print(D1[d]+D2[d])
        if D1[d] != 0xffff and D2[d] != 0xffff and  D1[d] + D2[d] > maxV:
            maxV = D1[d] + D2[d]

    # print(D1, D2)
    print('#{} {}'.format(tc, maxV))
    