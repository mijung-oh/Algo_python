import sys

# python3
# input = __import__('sys').stdin.readline
# sys.setrecursionlimit(10 ** 6)

from collections import deque 

def bfs(cur):
    # deque를 사용하여서 들어온 노드와 인접한 노드들을 deque에 담는다.
    # 인접노드이면서 color가 같은 경우 return false
    dq = deque()
    
    # 색칠한다.
    color[cur] = 0
    dq.append(cur)
    while dq:
        cur_node = dq.popleft()
        for i in graph[cur_node]:
            # 방문 안했을 경우
            if color[i] == -1:
                color[i] = 0 if color[cur_node] == 1 else 1
                dq.append(i)
            else:
                if color[i] == color[cur_node]:
                    return False


    return True

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    
    # 빨강: 0, 파랑: 1, 방문 안 했을 경우 -1
    color = [-1 for _ in range(V+1)]

    # 각각의 노드의 연결 정점을 넣어준다.
    graph = [[] for _ in range(V+1)]

    for e in range(E):
        a, b = map(int, input().split())

        # 1. graph에 저장 (양방향)
        graph[a].append(b)
        graph[b].append(a)

    check = True
    for i in range(1, V+1):
        if color[i] == -1:
            # print(i, color)
            if not bfs(i):
                check = not check
                break
    if check:
        print("YES")
    else:
        print("NO")