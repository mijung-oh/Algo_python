N = int(input())

# 무게, 키를 담을 배열
p = []
for n in range(N):
    p.append(list(map(int, input().split())))
# 등수 배열
result = [0 for x in range(N)]

for i in range(N):
    count = 0
    for j in range(N):
        if i != j and p[j][0] > p[i][0] and p[j][1] > p[i][1]:
            count += 1
    result[i] = count + 1
print(*result)
