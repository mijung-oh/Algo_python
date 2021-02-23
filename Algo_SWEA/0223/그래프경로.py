T = int(input())

def dfs(Go, Goal, Graph, visited):
    while 1:
        # 만나면 끝!
        if Go == Goal:
            return True
        # 경로가 0만 있는 경우
        if len(Graph[Go]) == 1:
            return False
        for i in Graph[Go]:
            # i가 0이 아닌 경우
            if i:
                # i번째 다녀간 표사ㅣ
                visited[i] = 1
                Go = i
                if dfs(i, Goal, Graph, visited):
                    return True
    return False


for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 1부터 시작
    Graph = [[0] for x in range(V+1)]
    visited = [False] * (V+1)

    # 그래프 값 저장하기
    for e in range(E):
        st, en = map(int, input().split())
        Graph[st].append(en)
    Go, Goal = map(int, input().split())
    if dfs(Go, Goal, Graph, visited):
        print('#{} {}'.format(tc, 1))
    else:
        print(('#{} {}'.format(tc, 0)))

