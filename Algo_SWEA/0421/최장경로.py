T = int(input())

def dfs(current, count):
    # print('ddd',current, count)
    global max_count

    if max_count < count:
        max_count = count

    visited[current] = 1

    for i in related_node[current]:
        if visited[i]: continue

        dfs(i, count+1)
        visited[i] = 0
    
    visited[current] = 0   
    return

for tc in range(1, T+1):
    node, edge  =map(int, input().split())
    
    # 1번노드~ n번노드
    related_node = [[] for _ in range(node+1)]
    visited = [0] * (node+1)

    for e in range(edge):
        node1, node2 = map(int, input().split())
        related_node[node1].append(node2)
        related_node[node2].append(node1)

    max_count = -1
    for n in range(1, node+1):
        dfs(n, 1)

    print('#{} {}'.format(tc, max_count))