N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
numbers.sort()
# 평균
print(round(sum(numbers) / N))
# 중앙값
mid = len(numbers) // 2
print(numbers[mid])
# 최빈값
pre = numbers[0]
n = [[1, pre]]
idx = 1
while idx < len(numbers):
    if numbers[idx] == pre:
        n[-1][0] += 1
        idx += 1
        continue
    n.append([1, numbers[idx]])
    pre = numbers[idx]
    idx += 1
m = -1
for i in n:
    if i[0] > m:
        m = i[0]
mm = []
for i in n:
    if i[0] == m:
        mm.append(i[1])
mm.sort()
if len(mm) > 1:
    print(mm[1])
else:
    print(mm[0])
# 간격
print(numbers[-1] - numbers[0])