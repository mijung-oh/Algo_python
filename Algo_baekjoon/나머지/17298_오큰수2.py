# 스택을 통해 인덱스로 접근한다.
# 먼저 answer 배열도 같이 만들어서 인덱스로 값을 넣는다.
# 일단 stack에는 0번 인덱스가 들어가있고,
# 바로 다음 인덱스와 비교하여서 큰지 확인한다.
# 만약 바로 다음 값이 더 클 경우, 스택에서 더 큰 값이 나올 때 까지 뺀다.
# 만약 가리키고 있는 포인터가 배열을 벗어났는데 스택이 비어있지 않으면
# 그 인덱스에 대한 값은 -1로 처리한다.


stack = [0]
N = int(input())
lst = list(map(int, input().split()))
answer = [0] * N
pointer = 0
while pointer < len(lst) - 1:
    # print(stack, "답", answer, pointer)
    if lst[pointer] < lst[pointer + 1]:
        # 오큰수를 찾음
        maxV = lst[pointer + 1]
        # stack을 돌면서 더 작으면 answer값 바꾸고 pop
        print(stack)
        for i in range(len(stack)-1, -1, -1):
            if lst[stack[i]] >= maxV:
                break
            answer[stack[i]] = maxV
            stack.pop()

    stack.append(pointer+1)
    pointer = stack[-1]

for i in stack:
    answer[i] = -1

print(answer)
print(*answer)
    