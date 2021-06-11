import heapq

def prim(cur, graph, U, D):
    heap = []
    heapq.heappush(heap, (0, cur))
    while heap:
        cost, cur = heapq.heappop(heap)
        U[cur] = 1
        for i in graph[cur]:
            if U[i[1]] == 0 and D[i[1]] > i[0]:
                D[i[1]] = i[0]
                heapq.heappush(heap, (i[0], i[1]))
    return sum(D)


def solution(n, costs):
    answer = 0
    
    # 방문한 노드
    U = [0] * n
    D = [0xffffffff] * n
    D[0] = 0
    graph = [[] for _ in range(n)]
    for c in costs:
        graph[c[0]].append((c[2], c[1]))
        graph[c[1]].append((c[2], c[0]))

    answer = prim(0, graph, U, D)
    return answer

l = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
print(solution(n, l))