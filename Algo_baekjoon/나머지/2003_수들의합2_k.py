N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(N):
    s = numbers[i]
    if s == M:
        result += 1
        continue
    elif s > M: continue

    for j in range(i+1, N):
        s += numbers[j]
        if s == M:
            result += 1
            break
        if s > M:
            break
print(result)
