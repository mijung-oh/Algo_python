# 연산자별 우선순위
inStack = {
    '+': 1,
    '*': 2,
    '(': 0,
}
outStack = {
    '+': 1,
    '*': 2,
    '(': 100,
}

def post(lst):
    stack = []
    result = []
    for l in lst:
        if l == '(' or l == '*':
            stack.append(l)
        elif l == '+':
            # 스택 탑이 +보다 우선순위가 높거나 스택이 비어있다면 그냥 추가
            if (len(stack) and stack[-1] == '(') or len(stack) == 0:
                stack.append(l)
            else:
                while 1:
                    if len(stack) and inStack[l] <= inStack[stack[-1]]:
                        result.append(stack.pop(-1))
                    else:
                        stack.append(l)
                        break
        elif l == ')':
            while 1:
                if len(stack):
                    k = stack.pop(-1)
                if k != '(':
                    result.append(k)
                elif k == '(':
                    break
        else:
            result.append(l)
    if len(stack):
        while len(stack):
            result.append(stack.pop(-1))
    return result





for tc in range(1, 11):
    N = int(input())
    lst = list(input())
    p = post(lst)
    stack = []
    # 후위표기식 계산
    for i in p:
        if i == '*' and len(stack) >= 2:
            en = stack.pop(-1)
            st = stack.pop(-1)
            stack.append(int(st) * int(en))
        elif i == '+' and len(stack) >= 2:
            en = stack.pop(-1)
            st = stack.pop(-1)
            stack.append(int(st) + int(en))
        else:
            stack.append(i)
    print('#{} {}'.format(tc, stack[-1]))


