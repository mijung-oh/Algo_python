prio = {}
prio['+'] = 1
prio['*'] = 2
for i in range(9):
    # 모든 숫자의 우선순위는 0
    prio[i] = 0

# 1. 후위표기식 만들기
for tc in range(1, 11):
    N = int(input())
    lst = list(input())

    # 후위표기식을 위한 스택
    stack = []
    post = ''
    for i in lst:
        if i == '+' or i == '*':
            # 스택안에 있는 연산자보다 우선순위가 높으면 그냥 스택에 넣음!
            if len(stack) == 0 or prio[stack[-1]] < prio[i]:
                stack.append(i)
            # 우선순위가 더 낮으면 계속 스택에서 빼고 post에 추가
            else:
                while 1:
                    if len(stack) and prio[stack[-1]] >= prio[i]:
                        post += stack[-1]
                        stack.pop(-1)
                    else:
                        stack.append(i)
                        break
        else:
            post += i
    # 스택에 남아있는 연산자들 모두 빼내기
    if len(stack):
        while stack:
            post += stack[-1]
            stack.pop(-1)


    # 2. 후위표기식을 통해 계산하기
    stack2 = []
    for p in range(len(post)):
        # p가 연산자이면
        if post[p] =='+' or post[p] == '*':
            # 스택에서 2개 원소빼기
            st = stack2[-1]
            stack2.pop(-1)
            en = stack2[-1]
            stack2.pop(-1)
            # 두 개 원소로 연산하고 stack2에 다시 넣기
            if post[p] == '+':
                stack2.append(st+en)
            else:
                stack2.append(st*en)
        else:
            stack2.append(int(post[p]))

    print('#{} {}'.format(tc, stack2[-1]))


