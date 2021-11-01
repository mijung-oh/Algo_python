import heapq
heap = []
node, edge = map(int, input().split())

graph = [[] for _ in range(node+1)]
visited = []
D = [0xffff for _ in range(node+1)]
min_cost = 0xffff
current = 0
for e in range(edge):
    st, en, cost = map(int, input().split())

    graph[st].append((cost, en))
    graph[en].append((cost, en))

    # 시작할 점 찾기
    # 가장 가중치가 작은 것을 찾아서 current 에 넣어준다.
    heapq.heappush(heap, (cost, st, en))
    heapq.heappush(heap, (cost, en, st))

current = heapq.heappop(heap)

def prim(current):
    if current in visited:
        return
    # current를 visited에 넣어준다.
    visited.append(current)
    print(visited)
    # D배열을 current에 맞게 초기화한다.
    for i in graph[current]:
        if D[i[1]] > i[0]:
            D[i[1]] = i[0]
    # 간선개수가 n-1이면 return
    if len(visited) == node-1:
        return

    
    mini = heapq.heappop(heap)
    prim(mini[1])
    heapq.heappush(heap, mini)
    mini = heapq.heappop(heap)
    # 가장 작은 가중치의 엣지를 구한다.
    # min_cost = 0xffff
    # min_node = 0
    # for i in range(1, len(graph)):
    #     # print(graph[i])
    #     for j in graph[i]:
    #         # 가려는 곳이 visited에 없으면서 최솟값이어야 한다.
    #         if j[1] in visited: continue

    #         if min_cost > j[0]:
    #             min_cost = j[0]
    #             min_node = j[1]

prim(current[2])


# prim(1)
total = 0
for i in range(1, len(D)):
    if D[i] != 0xffff:
        total += D[i]

print(D)
print(total)
