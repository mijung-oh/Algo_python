N, M = map(int, input().split())
sel = [0]*M
visited = [0]*N
arr = list(range(1, N+1))

def powerset(k,N, M):
    if k == M:
        print(*sel)
        return

    for i in range(N):
        if visited[i] != 1:
            visited[i] = 1
            sel[k] = arr[i]
            powerset(k+1, N, M)
            visited[i] = 0

powerset(0, N, M)