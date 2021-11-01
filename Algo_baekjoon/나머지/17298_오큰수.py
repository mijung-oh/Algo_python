# import heapq
# heap = []

N = int(input())
stack = list(map(int, input().split()))


# maxV, cur, top이 존재할 때
# cur < top인 경우, maxV는 여전히 -1
# cur > top인 경우, maxV에 cur을 넣어준다.

maxV = -1
result = [-1]
maxNumbers = []
while stack:
    cur = stack.pop()
    if stack and cur > stack[-1]:
        maxV = cur
        result.append(maxV)
        maxNumbers.append(maxV)

    elif stack and cur <= stack[-1]:
        if maxV <= stack[-1]:
            check = True
            for i in range(len(maxNumbers)-1, -1, -1):
                if maxNumbers[i] > stack[-1]:
                    check = False
                    result.append(maxNumbers[i])
                    break
            if check:
                result.append(-1)
        else:
            result.append(maxV)

# 출력
for r in range(len(result)-1, 0, -1):
    print(result[r], end=" ")
print(result[0], end="")