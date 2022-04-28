longS = list(input())
shortS = list(input())
stack = []

idx = 0
for s in longS:
    # stack에 문자 넣는다.
    stack.append(s)

    # 만약 현재 문자가 폭발 문자열의 마지막 문자라면
    if s == shortS[-1] and len(stack) >= len(shortS):
        # 폭발 문자열에 뒤에 껴 있는지 비교
        if ''.join(stack[len(stack)-len(shortS):]) == ''.join(shortS):
            # 폭발 문자열 길이만큼 stack에서 뺀다.
            l = len(shortS)
            while l:
                stack.pop()
                l -= 1

# 마지막 확인

if stack:
    print(''.join(stack))
else:
    print('FRULA')