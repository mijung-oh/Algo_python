T = int(input())

def dijk(current):
    global node
    if current == node: return

    # D배열을 current에 맞게 초기화한다.
    # graph => (가중치, 다음노드)
    for i in graph[current]:
        if i[1] in visited: continue

        if D[i[1]] > i[0] + D[current]:
            D[i[1]] = i[0] + D[current]
    # print(current, D)
    # 가장 작은 가중치의 엣지를 구한다.
    min_cost = 0xffff
    min_node = 0

    for idx, d in enumerate(D):
        # graph에는 (가중치, next node)
        # 가려는 곳이 visited에 없으면서 최솟값이어야 한다.
        if idx in visited: continue

        if min_cost > d:
            min_cost = d
            min_node = idx

    visited.append(min_node)
    dijk(min_node)
    

for tc in range(1, T+1):
    node, edge = map(int, input().split())

    graph = [[] for _ in range(node+1)]
    visited = []
    D = [0xffff for _ in range(node+1)]


    # 그래프 정보 받아서 그래프에 저장한다.
    # 그래프는 무방향 그래프이다.
    for e in range(edge):
        st, en, cost = map(int, input().split())
        graph[st].append((cost, en))

    # 시작노드 찾기
    current = 0
    D[current] = 0
    visited.append(current)
    dijk(current)

    total = D[node]
    # print(D)
    print('#{} {}'.format(tc, total))
