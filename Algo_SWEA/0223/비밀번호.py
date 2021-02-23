
for tc in range(1, 11):
    l, string = input().split()
    # string = '12344321'
    stack = []
    for s in range(len(string)):
        if len(stack) and stack[-1] == string[s]:
            stack.pop(-1)
            continue
        stack.append(string[s])


    print('#{} {}'.format(tc, ''.join(stack)))