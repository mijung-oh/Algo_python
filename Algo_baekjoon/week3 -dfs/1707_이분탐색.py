import sys
sys.setrecursionlimit(10 ** 6)

def dfs(changeColor, cur):
    # 색칠한다.
    color[cur] = changeColor
    for i in graph[cur]:
        if color[i] == -1:
            if not dfs(not changeColor, i):
                return False
        # 이미 색칠되어 있는 경우,
        # 현재 색칠된 색과 같으면 return false
        elif color[i] == changeColor:
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
            if not dfs(True, i):
                check = not check
                break
    if check:
        print("YES")
    else:
        print("NO")
    

     
