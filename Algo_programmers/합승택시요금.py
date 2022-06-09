from collections import deque
import sys
def solution(n, s, a, b, fares):
    answer = 0
    INF = sys.maxsize

    graph = [[] for _ in range(n+1)]

    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    # 스타트부터 각 노드까지의 최소거리로 업데이트한다.
    dist = [INF for _ in range(n+1)]
    q = deque()
    dist[0] = 0
    dist[s] = 0
    q.append(s)
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if dist[cur] + node[1] < dist[node[0]]:
                dist[node[0]] = dist[cur] + node[1]
                q.append(node[0])
                print(dist)



    return answer

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])