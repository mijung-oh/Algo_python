from collections import deque

N = int(input())
if N == 1:
    print(int(input()))
    exit()
    
exp = list(input())
result = -2147483649
numbers = [] # 3,8,7,9,2
ops = [] # +, *, -, *
for e in exp:
    if e in ['+', '-', '*']:
        ops.append(e)
    else:
        numbers.append(e)

def plus(x, y):
    return int(x)+int(y)

def minus(x,y):
    return int(x)-int(y)

def multiple(x,y):
    return int(x)*int(y)

def count(lst):
    lst = deque(list(lst))
    stack = deque()
    while lst:
        cur = lst.popleft()
        if cur == '(':
            a, op, b =  lst.popleft(), lst.popleft(), lst.popleft()
            if op == '+':
                stack.append(plus(a, b))
            elif op == '-':
                stack.append(minus(a, b))
            elif op == '*':
                stack.append(multiple(a, b))
        else:
            stack.append(cur)
    while len(stack) >= 3:
        a, op, b = stack.popleft(), stack.popleft(), stack.popleft()
        if op == '+':
            stack.appendleft(plus(a, b))
        elif op == '-':
            stack.appendleft(minus(a, b))
        elif op == '*':
            stack.appendleft(multiple(a, b))

    return stack[-1]  
    

def dfs(check, ope, idx):
    global result
    if idx == len(numbers)-1:
        ope += numbers[idx]
        result = max(result, count(ope))
        return
    # 만약 이전 숫자에서 괄호를 추가했다면
    if check:
        dfs(False, ope + str(numbers[idx]) + ops[idx], idx+1)
    else:
        # 괄호 추가하지 않음
        dfs(False, ope + str(numbers[idx]) + ops[idx], idx+1)
        
        # 괄호 추가
        if idx < len(numbers)-1:
            dfs(True, ope + "(" + str(numbers[idx]) + ops[idx], idx+1)
    
    return

dfs(False, "", 0)
print(result)