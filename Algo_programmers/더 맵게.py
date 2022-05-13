import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heapq.heappush(h, s)
        
    while h:
        a = heapq.heappop(h)
        if a >= K: break
        if not h: return -1
    
        answer += 1
        
        b = heapq.heappop(h)
        
        heapq.heappush(h, a + b * 2)
            
    return answer