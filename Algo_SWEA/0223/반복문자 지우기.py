T = int(input())
for tc in range(1, T+1):
    string = input()
    # string = 'abcd'
    stack = []

    for s in range(len(string)):
        if len(stack) and stack[-1] == string[s]:
            stack.pop(-1)
            continue
        stack.append(string[s])

    print('#{} {}'.format(tc, len(stack)))