from collections import deque

def solution(N, number):
    answer = 0
    INF = int(str(N) * 8)
    # 해당 숫자를 만드는데 필요한 숫자 개수
    dp = [0] * (INF+1)

    dp[N] = 1
    q = deque()
    for i in range(1, 9):
        dp[int(str(N)*i)] = i
        q.append(int(str(N)*i))
    
    while q:
        cur = q.popleft()
        if dp[cur] >= 7:
            continue
        if cur*N <= INF and (dp[cur*N] == 0 or dp[cur*N] > dp[cur] + 1):
            # if dp[cur]+1 > 8: continue
            dp[cur*N] = dp[cur]+1
            q.append(cur*N)

        if cur+N <= INF and (dp[cur+N] == 0 or dp[cur+N] > dp[cur] + 1):
            # if dp[cur]+1 > 8: continue
            dp[cur+N] = dp[cur]+1
            q.append(cur+N)

        if cur-N >= 0 and (dp[cur-N] == 0 or dp[cur-N] > dp[cur] + 1):
            # if dp[cur]+1 > 8: continue
            dp[cur-N] = dp[cur]+1
            q.append(cur-N)

        if dp[cur // N] == 0 or dp[cur // N] > dp[cur] + 1:
            # if dp[cur]+1 > 8: continue
            dp[cur // N] = dp[cur]+1
            q.append(cur // N)
    print(dp[number])
    return answer
solution(4, 31)