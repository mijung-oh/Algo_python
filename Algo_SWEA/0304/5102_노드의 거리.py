T = int(input())


def bfs():
    q = []
    q.append(start)
    print(start,end)
    while q:
        new = q.pop(0)
        for i in range(1, len(node[new])):
            # visited가 0인 경우에만
            if visited[node[new][i]] == 0:
                q.append(node[new][i])
                visited[node[new][i]] = visited[new]+1


for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0]*(V+1)

    # 1번부터 V번까지의 노드
    node = []
    for v in range(V+1):
        node.append([0])

    for e in range(E):
        st, en = map(int, input().split())
        node[st].append(en)
        node[en].append(st)
    # 출발지와 도착점
    start, end = map(int, input().split())

    bfs()
    print('#{} {}'.format(tc,visited[end]))