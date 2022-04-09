import sys
input = sys.stdin.readline
R, C = map(int, input().split())

BRD = [list(input()) for r in range(R)]

visited = [[0] * C for _ in range(R)]
alphabet = [0] * 26
result = -1
def dfs(r, c, cnt):
    global result
    for d in [(1,0), (0,1), (-1,0), (0,-1)]:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            # 해당 알파벳이 이전에 나온적이 없다면
            if not alphabet[ord(BRD[nr][nc]) - ord('A')]:
                visited[nr][nc] = 1
                alphabet[ord(BRD[nr][nc]) - ord('A')] = 1
                dfs(nr, nc, cnt+1)
                visited[nr][nc] = 0
                alphabet[ord(BRD[nr][nc]) - ord('A')] = 0
    result = max(result, cnt)
    return cnt

alphabet[ord(BRD[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(result)