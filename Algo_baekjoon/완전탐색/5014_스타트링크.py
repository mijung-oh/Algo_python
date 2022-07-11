import sys
F, S, G, U, D = map(int, input().split())

result = sys.maxsize
visited = [0] * (F+1)
visited[S] = 1
def dfs(cur, cnt):
    global F, S, G, U, D, result, visited
    if cnt > result:
        return

    if cur == G:
        result = min(result, cnt)
        return
    
    for move in [U, -D]:
        next_step = cur + move
        if 1 <= next_step <= F and not visited[next_step]:
                visited[next_step] = 1
                dfs(next_step, cnt+1)
                visited[next_step] = 0
    return

dfs(S, 0)
print(result if result != sys.maxsize else "use the stairs")