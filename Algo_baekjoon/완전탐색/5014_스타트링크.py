import sys
F, S, G, U, D = map(int, input().split())

result = sys.maxsize
visited = [0] * (F+1)
visited[S] = 1
def dfs(cur, cnt):
    global F, S, G, U, D, result, visited
    if cur == G:
        result = min(result, cnt)
        return
    
    for move in [U, -D]:
        if 1 <= cur + move <= F:
            if not visited[cur+move]:
                visited[cur+move] = 1
                dfs(cur+move, cnt+1)
                visited[cur+move] = 0
    return

dfs(S, 0)
print(result if result != sys.maxsize else "use the stairs")