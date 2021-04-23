T = int(input())

def dfs(value, count):
    print(value, count)
    global min_count, stack, M
    if value == M:
        if min_count > count:
            min_count = count
        return 

    if 100  < count:
        return
    if value > M - 10:
        return
    for i in range(4):
        # +1
        if i == 0:
            if (value+1) in stack: continue
            stack.append(value+1)
            dfs(value + 1, count + 1)
            stack.pop()

        # -1
        elif i == 2:
            if (value*2) in stack: continue
            stack.append(value*2)
            dfs(value * 2, count + 1)
            stack.pop()

        # *2
        elif i == 3:
            if (value-10) in stack: continue
            stack.append(value-10)
            dfs(value - 10, count + 1)
            stack.pop()

        # -10
        elif i == 1:
            if (value-1) in stack: continue
            stack.append(value-1)
            dfs(value - 1, count + 1)
            stack.pop()

    return



for tc in range(1, T+1):
    N, M = map(int, input().split())
    min_count = M-N
    stack = []
    dfs(N, 0)
    print(min_count)
    