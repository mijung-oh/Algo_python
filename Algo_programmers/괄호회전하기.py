from collections import deque

def solution(s):
    answer = 0
    # 회전은 0번부터 len(s)-1번 가능
    count = 0
    q = deque()
    for i in range(len(s)):
        q.append(s[i])
    bracket = {
        '}': '{', ']': '[', ')': '('
    }
    # 올바른 괄호 문자열인지 확인
    def isCollectString(s):
        # 처음부터 닫는 괄호일경우 올바른 괄호 문자열이 아님
        if s[0] in ['}', ']', ')']:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif stack and stack[-1] == bracket[s[i]]:
                stack.pop()
            
        if stack: return False
        return True
    
    # 0칸만큼 회전했을 경우
    if isCollectString(q):
        answer += 1
        
    while count < len(s)-1:
        count += 1
        q.append(q.popleft())
        if isCollectString(q):
            answer += 1
    return answer