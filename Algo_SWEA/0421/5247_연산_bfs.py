from collections import deque

T = int(input())

def bfs(value, count):
    global M, min_count
    dq = deque()
    dq.append((value, count))    

    while dq:
        current = dq.popleft()
        # current - (현재 계산된 값, 현재까지의 카운트)
        c = [current[0]*2, current[0]+1, current[0]-10, current[0]-1]

        for newV in c:            
            if newV > 1000000: continue

            if newV == M:
                if current[1] + 1 < min_count:
                    min_count = current[1] + 1
            else:
                if current[1] + 1< min_count:
                    if visited[newV]:
                        continue
                    visited[newV] = 1
                    dq.append((newV, current[1]+1))
                    
    return



for tc in range(1, T+1):
    N, M = map(int, input().split())
    min_count = 0xffff
    visited = [0] * 1000001
    bfs(N, 0)
    print('#{} {}'.format(tc, min_count))
    