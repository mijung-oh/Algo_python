N = int(input())
numbers = list(map(int, input().split()))
A = list(map(int, input().split()))
B = ['+', '-', '*', '/']
minV = 1e9
maxV = -1e9

ops = []
for idx, a in enumerate(A):
    while a:
        ops.append(B[idx])
        a -= 1


def cal(total, idx, add, minus, mul, division):
    global minV, maxV
    if idx >= len(numbers):
        maxV = max(maxV, total)
        minV = min(minV, total)
        return

    if add:
        cal(total + numbers[idx], idx+1, add-1, minus, mul, division)
    if minus:
        cal(total - numbers[idx], idx+1, add, minus-1, mul, division)
    if mul:
        cal(total * numbers[idx], idx+1, add, minus, mul-1, division)
    if division:
        cal(int(total / numbers[idx]), idx+1, add, minus, mul, division-1)

cal(numbers[0], 1, A[0], A[1], A[2], A[3])
print(maxV)
print(minV)

