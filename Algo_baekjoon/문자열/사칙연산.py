def solution(N, number):
    answer = 10
    INF = N ** 8 + 1
    dp = [10 for _ in range(INF)]
    
    def dfs(cur, cnt):
        if cnt > 8: return
        if cur == number:
            print(cnt)
            answer = min(answer, cnt)
            return
    
        if cur+cur < INF and dp[cur+cur] > cnt + 1:
            dp[cur+cur] = cnt+1
            dfs(cur+cur, cnt+1)
        if cur * cur < INF and dp[cur*cur] > cnt + 1:
            dp[cur*cur] = cnt+1
            dfs(cur*cur, cnt+1)
        if cur - cur < INF and dp[cur-cur] > cnt + 1:
            dp[cur-cur] = cnt+1
            dfs(cur-cur, cnt+1)
        if cur and cur // cur < INF and dp[cur//cur] > cnt + 1:
            dp[cur//cur] = cnt+1
            dfs(cur//cur, cnt+1)
        
    dp[N] = 1
    dfs(N, 0)
    return answer
solution(5, 12)