from collections import deque

def solution(number, k):
    answer = []
    cur = 0
    # 첫 번째 숫자는 가장 큰 숫자로
    m = -1
    m_idx = -1
    for i in range(len(number)):
        if int(number[i]) > m:
            m = int(number(m_idx))
            m_idx = i
    answer.append(number[m_idx])
    k -= m_idx
    
    q = deque()
    for i in range(m_idx+1, len(number)):
        q.append(number[i])
    
            
    return answer