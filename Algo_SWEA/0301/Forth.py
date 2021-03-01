T = int(input())

for tc in range(1, T+1):
    lst = input().split()
    stack = []
    for i in range(len(lst)):
        # 숫자인 경우
        if lst[i] != '*' and lst[i] != '+' and lst[i] != '-' and lst[i] != '/' and lst[i] != '.':
            stack.append(lst[i])
        elif lst[i] == '.':
            if len(stack) == 0 or len(stack) > 1:
                print('#{} {}'.format(tc, 'error'))
                break
            a = stack.pop(-1)
            print('#{} {}'.format(tc, a))
            break
        else:
            if len(stack) <= 1:
                print('#{} {}'.format(tc, 'error'))
                break
            en = stack.pop(-1)
            st = stack.pop(-1)
            if lst[i] == '*':
                r = int(st) * int(en)
                stack.append(str(r))
            elif lst[i] == '+':
                r = int(st) + int(en)
                stack.append(str(r))
            elif lst[i] == '-':
                r = int(st) - int(en)
                stack.append(str(r))
            elif lst[i] == '/':
                r = int(st) // int(en)
                stack.append(str(r))