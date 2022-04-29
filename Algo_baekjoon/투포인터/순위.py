from collections import deque

def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for r in results:
        a, b = r
        # a가 b를 이김 == b가 a한테 짐
        win[a].append(b)
        lose[b].append(a)
    
    def check_win(t):
        cnt = 0
        q = deque()
        q.append(t)
        visited = [0] * (n+1)
        while q:
            cur = q.popleft()
            for w in win[cur]:
                if not visited[w]:
                    visited[w] = 1
                    cnt += 1
                    q.append(w)
        return cnt
     
    def check_lose(t):
        cnt = 0
        q = deque()
        q.append(t)
        visited = [0] * (n+1)
        while q:
            cur = q.popleft()
            for w in lose[cur]:
                if not visited[w]:
                    visited[w] = 1
                    cnt += 1
                    q.append(w)
        return cnt
        
    for s in range(1, n+1):
        if check_win(s) + check_lose(s) == n-1:
            answer += 1
    return answer