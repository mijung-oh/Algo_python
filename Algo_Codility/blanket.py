def solution(S):
    stack = []
    d = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for s in S:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        elif s == '}' or s == ']' or s == ')':
            if stack and stack[-1] == d[s]:
                stack.pop(-1)
            else:
                return 0
    if stack: return 0
    return 1

print(solution('{}}'))
        