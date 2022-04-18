from collections import deque
def solution(n, edge):
    answer = 0
    lines = [9999999 for _ in range(n+1)]
    lines[1] = 0
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
        
    q = deque()
    q.append(1)
    while q:
        cur = q.popleft()
        if cur in graph.keys():
            # 현재 cur과 연결되어있는 노드의 lines 값과 lines[cur]+1과 비교하여서
            # 더 작은 값으로 초기화한다.
            for node in graph[cur]:
                if lines[node] > lines[cur]+1:
                    lines[node] = lines[cur]+1
                    q.append(node)
    max_v = -1
    for l in lines:
        if l == 9999999 or not l: continue
        if l and max_v < l:
            max_v = l
            answer = 1
        else: answer += 1
    print(lines)
    print(answer)
    return answer
solution(5, [[2,3]])