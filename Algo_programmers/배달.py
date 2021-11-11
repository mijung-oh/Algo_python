def solution(N, road, K):
    answer = 0
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)]
    D = [10000] * (N+1)
    
    result = [0] * (N+1)
    visited = [0] * (N+1)

    for r in road:
        st, en, w = r
        if not graph[st][en] or (graph[st][en] and w < graph[st][en]):
            graph[st][en] = w
            graph[en][st] = w
            graph2[st].append(en)
            graph2[en].append(st)

    
    def dfs(n, w):
        nonlocal N, K

        if D[n] > w:
            D[n] = w

        # if w <= K and not result[n]:
        #     result[n] = 1

        for i in graph2[n]:
            # 길이 있는 경우
            if not visited[i]:
                if w+graph[n][i] <= K and w+graph[n][i] < D[i]:
                    visited[i] = 1
                    dfs(i, w+graph[n][i])
                    visited[i] = 0            
        return    

    visited[1] = 1
    dfs(1, 0)
    for i in D:
        if i < 10000:
            answer += 1
    print(answer)
    return answer
solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)