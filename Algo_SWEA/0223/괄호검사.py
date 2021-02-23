T = int(input())

for tc in range(1, T+1):
    stack = list(input())
    # 빼낸 괄호만 담을 스택
    stack2 = []
    # 중간에 닫힌 괄호가 아닌 경우 check=0이됨
    check = 1
    while len(stack):
        if stack[-1] == ')':
            stack2.append(')')
            stack.pop()
        elif stack[-1] == '}':
            stack2.append('}')
            stack.pop()
        # ()
        elif stack[-1] == '(':
            if len(stack2) and stack2[-1] == ')':
                stack.pop()
                stack2.pop()
            else:
                check = 0
                break
        # {}
        elif stack[-1] == '{':
            if len(stack2) and stack2[-1] == '}':
                stack.pop()
                stack2.pop()
            else:
                check = 0
                break
        else:
            stack.pop()
    if check and len(stack2) == 0:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))