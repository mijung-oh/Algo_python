import sys
sys.setrecursionlimit(1000000)
def solution(n, edge):
    answer = 0
    graph = dict()
    for e in edge:
        l, r = e[0], e[1]
        if l in graph.keys():
            graph[l].append(r)
        else:
            graph[l] = [r]
        
        if r in graph.keys():
            graph[r].append(l)
        else:
            graph[r] = [l]

    # 1번부터 거치는 간선 개수를 저장하는 배열을 만든다.
    lines = [999999] * (n+1)
    # 해당 노드를 방문했는지 체크
    visited = [0] * (n+1)

    # dfs로 간선 개수를 저장한다.
    def dfs(cur, cnt):
        if cur not in graph.keys():
            return
        for node in graph[cur]:
            if not visited[node] and lines[node] > cnt+1:
                visited[node] = 1
                lines[node] = cnt+1
                dfs(node, cnt+1)
                visited[node] = 0
        return
    visited[1] = 1
    lines[1] = 0
    dfs(1, 0)
    max_l = 0
    for v in lines:
        if v != 999999 and v > max_l:
            answer = 1
            max_l = v
        else: answer += 1
        
    print(lines)
    print(answer)
    return answer


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])