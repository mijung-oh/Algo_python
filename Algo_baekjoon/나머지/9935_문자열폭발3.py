total = list(input())
pang = input()

stack = []

for i in range(len(total)):
    check = True
    stack.append(total[i])

    # 마지막 문자가 현재 문자와 일치하면
    # 스택에 있는 값들을 하나씩 뽑아내서 폭탄문자열과 같은지 확인한다.
    if stack[-1] ==pang[-1]:
        if len(stack) >= len(pang):
            for j in range(len(pang)):
                if pang[-1-j] != stack[-1-j]:
                    check = False
            if check:
                # 같은 값이면 그만큼 stack에서 빼준다.
                for j in range(len(pang)):
                    stack.pop()
       

if stack:
    print(''.join(stack))
else:
    print("FRULA")