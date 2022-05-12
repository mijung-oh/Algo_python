def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(cur):
        for i in range(len(computers[cur])):
            if cur != i and computers[cur][i] and not visited[i]:
                visited[i] = 1
                dfs(i)
        return
        
    # 시작점
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            dfs(i)


    return answer