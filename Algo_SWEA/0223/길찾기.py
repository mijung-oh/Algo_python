goal = 99

def dfs(go, graph, visited):
    # while 1:
    if go == goal:
        return True
    # 갈 수 있는 경로가 없는 경우 -> [-1]으로 저장되어있는 경우
    if len(graph[go]) == 1:
        return False
    for tg in graph[go]:
        if tg != -1 and visited[tg] == False:
            visited[tg] = True
            go = tg
            if dfs(go, graph, visited):
                return True
    return False





for i in range(10):
    tc, N = map(int, input().split())
    pair = list(map(int, input().split()))
    go = 0
    # 1번부터 99번까지
    graph = [[-1] for x in range(100)]
    visited = [False]*100

    # 그래프 완성하기
    for p in range(0, len(pair), 2):
        st = pair[p]
        en = pair[p+1]
        print(st, en)
        graph[st].append(en)
    if dfs(go, graph, visited):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))


