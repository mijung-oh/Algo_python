# 피연산자는 바로 출력
# 연산자는 스택에 push해서 수식이 끝나면 한번에 출력
string = '2+3*4/5'
stack = []
result = []
for s in string:
    if s == '*' or s == '+' or s == '/':
        stack.append(s)
    else:
        result.append(s)

while stack:
    result.append(stack[-1])
    stack.pop()

print(*result)