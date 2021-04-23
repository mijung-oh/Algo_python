import heapq
T = int(input())

def prim(current):

    for i in graph[current]:
        heapq.heappush(heap, i)

    while heap:
        for i in graph[current]:
            if i[1] in visited: continue

            if D[i[1]] > i[0]:
                D[i[1]] = i[0]
        # next
        c = heapq.heappop(heap)

        current = c[1]
        if current in visited: continue
        visited.append(current)
        print(visited,D)
        for i in graph[current]:
            heapq.heappush(heap, i)

    return

for tc in range(1, T+1):
    heap = []
    node, edge = map(int, input().split())

    graph = [[] for _ in range(node+1)]
    visited = []
    D = [0xffff for _ in range(node+1)]


    # 그래프 정보 받아서 그래프에 저장한다.
    # 그래프는 무방향 그래프이다.
    for e in range(edge):
        st, en, cost = map(int, input().split())

        graph[st].append((cost, en))
        graph[en].append((cost, st))

    # visited.append(0)
    D[1] = 0
    prim(1)
    total = 0
    for i in range(1, len(D)):
        if D[i] != 0xffff:
            total += D[i]

    print('#{} {}'.format(tc, total))
