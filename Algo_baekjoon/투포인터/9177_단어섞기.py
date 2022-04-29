import sys
input = sys.stdin.readline

N = int(input())

def dfs(a, b, c, A, B, C, visited):
    # 만약 c 문자열 탐색이 끝났다면
    if c >= len(C):
        return True

    if a >= len(A) and B[b:] == C[c:]:
        return True
    if b >= len(B) and A[a:] == C[c:]:
        return True

    # 현재 A와 B 제일 앞 단어랑 C 앞 단어와 같을 경우
    if a < len(A) and b < len(B) and A[a] == C[c] and B[b] == C[c]:
        if not visited[c+1]:
            visited[c+1] = 1
            if dfs(a+1, b, c+1, A, B, C, visited): return True
            if dfs(a, b+1, c+1, A, B, C, visited): return True
            visited[c+1] = 0
    # A 첫 단어와 C 첫 단어가 같은 경우
    elif a < len(A) and A[a] == C[c]:
        if not visited[c+1]:
            visited[c+1] = 1
            if dfs(a+1, b, c+1, A, B, C, visited): return True
            visited[c+1] = 0
    # B 첫 단어와 C 첫 단어가 같은 경우
    elif b < len(B) and B[b] == C[c]:
        if not visited[c+1]:
            visited[c+1] = 1
            if dfs(a, b+1, c+1, A, B, C, visited): return True
            visited[c+1] = 0

    return False
    
# 1000
for n in range(N):
    A, B, C = input().split()
    visited = [0] * len(C)
    visited[0] = 1
    if dfs(0, 0, 0, A, B, C, visited):
        print("Data set ", n+1, ": yes")
    else:
        print("Data set ", n+1, ": no")
    