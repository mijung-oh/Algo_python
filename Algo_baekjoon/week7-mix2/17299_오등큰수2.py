N = int(input())
num = list(map(int, input().split()))

# 오른쪽에 있으면서, 등장 횟수가 큰 것
count = {}
for i in num: # O(1,000,000)
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

result = [-1] * N
stack = [0]

for i in range(N):
    while stack and count[num[stack[-1]]] < count[num[i]]:
        result[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)

print(*result)
            

