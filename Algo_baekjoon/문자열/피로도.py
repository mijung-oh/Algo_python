import heapq

def solution(n, works):
    answer = 0
    h = []
    for work in works:
        heapq.heappush(h, -work)
    while n and h:
        cur = -heapq.heappop(h)
        cur -= 1
        n -= 1
        if cur == 0: continue
        heapq.heappush(h, -cur)
    
    return answer
solution(3, [1,1])