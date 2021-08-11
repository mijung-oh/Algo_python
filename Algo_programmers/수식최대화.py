from collections import deque

def combi(arr):
    n = len(arr)
    result = []
    for i in range(1<<n):
        t = []
        for j in range(n):
            if i & (1<<j):
                t.append(arr[j])
        print(t)
        if len(t) == n:
            result.append(t)
    return result

def counter(pre, post, op):
    if op == "*": return pre * post
    elif op == "+": return pre + post
    else: return pre - post


def two(numbers, prio, set_prio):
    maxV = -1
    stack = []
    queue = deque()

    for higher in set_prio:
        result = 0
        # 나온 연산자가 higer이면 계산한 후 다시 넣기
        for i in range(len(prio)):
            stack.append(numbers[i])
            stack.append(prio[i])
        stack.append(numbers[-1])
        while stack:
            # print(stack, queue)
            if len(stack) == 1:
                queue.append(stack.pop())
                continue

            stack_sum = 0
            post = stack.pop()
            op = stack.pop()

            if op == higher:
                pre = stack.pop()
                value = counter(pre,post, op)
                # print(value)
                stack.append(value)
            else:
                queue.append(post)
                queue.append(op)

        while len(queue) > 1:
            # print(queue)
            pre = queue.popleft()
            op = queue.popleft()
            post = queue.popleft()
            value = counter(pre, post, op)
            queue.appendleft(value)
        result = queue.popleft()

        if maxV < abs(result):
            maxV = abs(result)

    return maxV

        
                
def three(numbers, prio, set_prio):
    maxV = -1
    stack = []
    second_queue = deque()
    three_queue = deque()

    for higher in set_prio:
        result = 0
        # 나온 연산자가 higer이면 계산한 후 다시 넣기
        for i in range(len(prio)):
            stack.append(numbers[i])
            stack.append(prio[i])
        stack.append(numbers[-1])
        while stack:
            # print(stack, queue)
            if len(stack) == 1:
                queue.append(stack.pop())
                continue

            stack_sum = 0
            post = stack.pop()
            op = stack.pop()

            if op == higher:
                pre = stack.pop()
                value = counter(pre,post, op)
                # print(value)
                stack.append(value)
            else:
                queue.append(post)
                queue.append(op)

        while len(queue) > 1:
            # print(queue)
            pre = queue.popleft()
            op = queue.popleft()
            post = queue.popleft()
            value = counter(pre, post, op)
            queue.appendleft(value)
        result = queue.popleft()

        if maxV < abs(result):
            maxV = abs(result)

    return maxV




def solution(expression):
    answer = 0
    numbers = []

    ops = ["*", "+", "-"]
    prios = {
        "*": 0,
        "+": 0,
        "-": 0,
    }
    
    prio = []
    sub = ''
    for e in expression:
        if e in ops:
            numbers.append(int(sub))
            prio.append(e)
            prios[e] += 1
            sub = ''
            continue
        sub += e
    numbers.append(int(sub))
    # 연산자가 2가지 종류일 경우
    # 경우의 수는 2가지
    if list(prios.values()).count(0) == 1:
        two(numbers, prio, set(prio))

    return answer

solution("50*6-3*2")